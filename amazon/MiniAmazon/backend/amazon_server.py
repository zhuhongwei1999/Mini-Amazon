import threading
import socket
from world_amazon_pb2 import *
from handle import *
from django.core.wsgi import get_wsgi_application
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(project_root)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MiniAmazon.settings')
application = get_wsgi_application()
from amazon_web.models import *

WORLD = {'hostname': "vcm-31112.vm.duke.edu", 'port': 23456}
UPS = {'hostname': "vcm-30676.vm.duke.edu", 'port': 22222}

if __name__ == '__main__':
    socket_world = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_world.connect((socket.gethostbyname(WORLD["hostname"]), WORLD["port"]))
    socket_ups = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_ups.connect((socket.gethostbyname(UPS["hostname"]), UPS["port"]))
    world_id = connectWorld(socket_world)
    print('Connest to UPS successfully.')
    u_connect = AInformWorld()
    u_connect.worldid = world_id
    send_msg(socket_ups, u_connect)
    print('World ID send successfully.')
    
    Order.objects.all().update(status='checked_out', truck_id = None)
    world_send = threading.Thread(target = sendToWorld, args = (socket_world,))
    world_recv = threading.Thread(target = recvFromWorld, args = (socket_world,))
    ups_send = threading.Thread(target = sendToUPS, args = (socket_ups,))
    ups_recv = threading.Thread(target = recvFromUPS, args = (socket_ups,))
    
    world_send.start()
    world_recv.start()
    ups_send.start()
    ups_recv.start()