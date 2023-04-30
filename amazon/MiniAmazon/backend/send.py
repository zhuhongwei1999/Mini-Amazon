from handle import *

order = Order.objects.get(tracking_num=58)
send_shipped_email(order.user.email, order.user.username, order.__str__())
send_delivered_email(order.user.email, order.user.username, order.__str__())