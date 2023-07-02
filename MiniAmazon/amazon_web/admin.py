from django.contrib import admin
from .models import Product, Warehouse, Order, Cart, OrderItem

# Register your models here.
admin.site.register(Product)
admin.site.register(Warehouse)
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(OrderItem)