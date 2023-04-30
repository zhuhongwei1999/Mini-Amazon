from django.db import models
from django.contrib.auth.models import User

ORDER_STATUS_CHOICES = [
    ('checked_out', 'checked_out'),
    ('requesting_inventory','requesting_inventory'),
    ('inventory_arrived','inventory_arrived'),
    ('packing', 'packing'),
    ('packed', 'packed'),
    ('booked_truck', 'booked_truck'),
    ('truck_arrived', 'truck_arrived'),
    ('loading', 'loading'),
    ('loaded', 'loaded'),
    ('delivering', 'delivering'),
    ('delivered', 'delivered'),
]

# Create your models here.

class Warehouse(models.Model):
    whid = models.IntegerField(primary_key=True, default=1)
    x = models.IntegerField(default=10)
    y = models.IntegerField(default=10)

    def __str__(self) -> str:
        return f'Warehouse {self.whid}'

class Product(models.Model):
    product_id = models.IntegerField(primary_key=True, default=1)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(max_length=100)
    store = models.CharField(max_length=100)
    sales = models.IntegerField()
    delivery = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='products/', default='products/default.jpg')
    inventory = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name} Product'

class Order(models.Model):
    tracking_num = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    total_price = models.FloatField()
    status = models.CharField(max_length=50, choices=ORDER_STATUS_CHOICES, default='checked_out')
    whid = models.IntegerField(default=1)
    truck_id = models.IntegerField(null=True)

    def __str__(self):
        product_list = [f'{item.product.name} x{item.quantity}' for item in self.order_items.all()]
        products = ', '.join(product_list)
        return f"Order ID: {self.tracking_num}\n Products: {products}\n Total Price: {self.total_price}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    stars = models.FloatField(default=5.0)

    def __str__(self):
        return f"{self.product.name} - {self.quantity} pcs"

    @property
    def subtotal(self):
        return round(self.product.price * self.quantity, 1)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'

    @property
    def subtotal(self):
        return round(self.product.price * self.quantity, 1)