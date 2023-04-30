import threading
from world_amazon_pb2 import *
from amazon_ups_pb2 import *
import os
import sys
from django.core.wsgi import get_wsgi_application
import time
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(project_root)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MiniAmazon.settings')
application = get_wsgi_application()
from amazon_web.models import *
from django.conf import settings
from django.core.mail import send_mail
from google.protobuf.internal.decoder import _DecodeVarint32
from google.protobuf.internal.encoder import _EncodeVarint

seq = 1
toWorld = {}
toworld_lock = threading.Lock()
toUPS = {}
toUPS_lock = threading.Lock()

def connectWorld(socket_world):
  conn = AConnect()
  conn.isAmazon = True
  wh_info = Warehouse.objects.get(whid=1)
  warehouse = conn.initwh.add()
  warehouse.id = 1
  warehouse.x = wh_info.x
  warehouse.y = wh_info.y
  send_msg(socket_world, conn)
  connect_reply = AConnected()
  connect_reply.ParseFromString(recv_msg(socket_world))
  print("world id: " + str(connect_reply.worldid))
  print("result: " + str(connect_reply.result))
  return connect_reply.worldid

def sendToWorld(socket_world):
  global seq
  while True:
    orders = Order.objects.filter(status='checked_out').values_list('tracking_num', flat=True).distinct()
    for tracking_num in orders:
      order_items = OrderItem.objects.filter(order__tracking_num=tracking_num).values('product_id', 'quantity', 'product__name')
      for item in order_items:
        a_commands = ACommands()
        a_commands.disconnect = False
        a_purchase_more = APurchaseMore()
        a_purchase_more.whnum = 1
        with toworld_lock:
          a_purchase_more.seqnum = seq
          toWorld[seq] = a_commands
          seq += 1
        product = a_purchase_more.things.add()
        product.id = item['product_id']
        product.description = item['product__name']
        product.count = item['quantity']
        a_commands.buy.append(a_purchase_more)
        Order.objects.filter(tracking_num=tracking_num).update(status='requesting_inventory')
            
    with toworld_lock:
      toWorldCopy = dict(toWorld)
      for key in toWorldCopy:
        send_msg(socket_world, toWorldCopy[key])
 
def sendToUPS(socket_UPS):
  while True:
    with toUPS_lock:
      messages_to_send = {}
      for key in toUPS:
        messages_to_send[key] = toUPS[key]
      toUPS.clear()
    for key, message in messages_to_send.items():
      # print(message)
      time.sleep(3)
      send_msg(socket_UPS, message)

def recvFromWorld(socket_world):
  global seq
  while True:
    message = recv_msg(socket_world)
    if message == "":
      continue
    world_response = AResponses()
    world_response.ParseFromString(message)
    with toworld_lock:
      for ack in world_response.acks:
        if ack in toWorld:
          toWorld.pop(ack)

    # Handle Error
    for error in world_response.error:
      print("Received An Error!")
      print("Message: " + str(error.err))
      print("Origin seqnum: " + str(error.originseqnum))
      print("Error seqnum: " + str(error.seqnum))
      send_ack(socket_world, error.seqnum)

    # Handle repeated APurchaseMore arrived = 1;
    for arrive in world_response.arrived:
      send_ack(socket_world, arrive.seqnum)
      for item in arrive.things:
        product = Product.objects.get(product_id=item.id)
        product.inventory += item.count
        product.save()
    
    # Check Inventory
    if len(Order.objects.filter(status='requesting_inventory')) > 0:
      for order in Order.objects.filter(status='requesting_inventory'):
        all_available = True
        for item in order.order_items.all():
          if item.product.inventory < item.quantity:
            all_available = False
            break
        if all_available:
          order.status = 'inventory_arrived'
          order.save()
          with toworld_lock:
            a_pack = createAPack(order)
            toWorld[seq] = a_pack
            seq = seq + 1
            order.status = 'packing'
            order.save()

    # Handle repeated APacked ready = 2;
    for pack in world_response.ready:
      send_ack(socket_world, pack.seqnum)
      with toUPS_lock:
        order = Order.objects.get(tracking_num=pack.shipid)
        order.status = 'packed'
        order.save()
        a_book_truck = createABookTruck(order)
        toUPS[seq] = a_book_truck
        seq = seq + 1
        order.status = 'booked_truck'
        order.save()

    # Handle repeated ALoaded loaded = 3;
    for load in world_response.loaded:
      send_ack(socket_world, load.seqnum)
      with toUPS_lock:
        order = Order.objects.get(tracking_num=load.shipid)
        order.status = 'loaded'
        order.save()
        a_start_deliver = createAStartDeliver(order)
        toUPS[seq] = a_start_deliver
        seq += 1
        order.status = 'delivering'
        order.save()
        send_shipped_email(order.user.email, order.user.username, order.__str__())

    # Handle repeated APackage packagestatus = 7;
    for packagestatus in world_response.packagestatus:
      send_ack(socket_world, packagestatus.seqnum)

def recvFromUPS(socket_UPS):
  global seq
  while True:
    message = recv_msg(socket_UPS)
    if message == "":
      continue
    ups_response = UACommunication()
    ups_response.ParseFromString(message)
    
    # Handle repeated UTruckArrived arrived = 1;
    for arrive in ups_response.arrived:
      tracking_num = Order.objects.get(tracking_num=arrive.packageid).tracking_num
      print("Recv UTruckArrived: " + str(tracking_num))
      with toworld_lock:
        order = Order.objects.get(tracking_num=arrive.packageid)
        order.status = 'truck_arrived'
        order.truck_id = arrive.truckid
        order.save()
        a_load = createAPutOnTruck(order)
        toWorld[seq] = a_load
        seq += 1
        order.status = 'loading'
        order.save()
        
    # Handle repeated UDelivered delivered = 2;
    for deliver in ups_response.delivered:
      tracking_num = Order.objects.get(tracking_num=deliver.packageid).tracking_num
      print("Recv UDelivered: " + str(tracking_num))
      with toUPS_lock:
        order = Order.objects.get(tracking_num=deliver.packageid)
        order.status = 'delivered'
        order.save()
        send_delivered_email(order.user.email, order.user.username, order.__str__())

def createAPack(order):
  order_items = order.order_items.all()
  Acmd = ACommands()
  apack = Acmd.topack.add()
  apack.whnum = 1
  apack.shipid = order.tracking_num
  apack.seqnum = seq
  for item in order_items:
    a_product = apack.things.add()
    a_product.id = item.product.product_id
    a_product.description = item.product.name
    a_product.count = item.quantity
  print("Created APack: " + str(order.tracking_num))
  return Acmd

def createABookTruck(order):
  warehouse = Warehouse.objects.get(whid=order.whid)
  user_info = order.user.profile
  AUcmd = AUCommunication()
  book_truck = AUcmd.bookings.add()
  book_truck.packageid = order.tracking_num
  book_truck.warehouseid = order.whid
  book_truck.warehousex = warehouse.x
  book_truck.warehousey = warehouse.y
  book_truck.destinationx = user_info.default_x
  book_truck.destinationy = user_info.default_x
  if user_info.ups_account:
    book_truck.upsid = user_info.ups_account
  print("Created ABookTruck: " + str(order.tracking_num))
  return AUcmd

def createAPutOnTruck(order):
  Acmd = ACommands()
  a_load = Acmd.load.add()
  a_load.whnum = order.whid
  a_load.truckid = order.truck_id
  a_load.shipid = order.tracking_num
  a_load.seqnum = seq
  print("Created APutOnTruck: " + str(order.tracking_num))
  return Acmd

def createAStartDeliver(order):
  AUcmd = AUCommunication()
  start_deliver = AUcmd.delivers.add()
  start_deliver.packageid = order.tracking_num
  print("Created AStartDeliver: " + str(order.tracking_num))
  return AUcmd


def send_ack(socket, ack):
  a_commands = ACommands()
  a_commands.acks.append(ack)
  a_commands.disconnect = False
  send_msg(socket, a_commands)

def send_msg(socket, msg):
  to_send = msg.SerializeToString()
  _EncodeVarint(socket.sendall, len(to_send), None)
  socket.sendall(to_send)
  
def recv_msg(socket):
  var_int_buff = []
  while True:
    buf = socket.recv(1)
    var_int_buff += buf
    if not buf:
      return ""
    try:
      msg_len, new_pos = _DecodeVarint32(var_int_buff, 0)
    except IndexError:
      continue
    if new_pos != 0:
      break
  whole_message = socket.recv(msg_len)
  return whole_message

def send_delivered_email(user_email,user_name,request_details):
  subject = 'Order Delivered'
  message = 'Dear '+ user_name +',\n\nYour order has been successfully delivered!\n\nDetails:\n' + request_details + '\n\nBest regards,\nAmazon'
  email_from = settings.EMAIL_HOST_USER
  recipient_list = [user_email]
  send_mail(subject, message, email_from, recipient_list)
    
def send_shipped_email(user_email,user_name,request_details):
  subject = 'Order Shipped'
  message = 'Dear '+ user_name +',\n\nYour order is on the way!\n\nDetails:\n' + request_details + '\n\nBest regards,\nAmazon'
  email_from = settings.EMAIL_HOST_USER
  recipient_list = [user_email]
  send_mail(subject, message, email_from, recipient_list)
  
