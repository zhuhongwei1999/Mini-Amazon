# myapp/management/commands/populate_products.py

from django.core.management.base import BaseCommand
from amazon_web.models import Product,Warehouse

class Command(BaseCommand):
    help = 'Populate the product table with data'

    def handle(self, *args, **options):
        # generate data and save it to the database
        if not Product.objects.exists():
            Product.objects.create(product_id = 1, name='Apple Watch', price=329.0, store='Apple', category='Electronics', sales=24125, delivery='Free Delivery',picture='products/apple.jpg')
            Product.objects.create(product_id = 2, name='Yoga Mat', price=59.5, store='Liforme', category='Sports', sales=2131, delivery='Free Delivery', picture = 'products/yoga.jpg')
            Product.objects.create(product_id = 3, name='Running Shoes', price=78.0, store='Nike', category='Sports', sales=128, delivery='Free Delivery', picture = 'products/shoes.jpg')
            Product.objects.create(product_id = 4, name='Sofa', price=699.0, store='Honbay', category='Home/DIY', sales=178, delivery='Free Delivery', picture = 'products/sofa.jpg')
            Product.objects.create(product_id = 5, name='Air Purifier', price=309.0, store='Molekule', category='Home/DIY', sales=786, delivery='Free Delivery', picture = 'products/air.jpg')
            Product.objects.create(product_id = 6, name='Wall Art', price=69.9, store='72Pcs', category='Home/DIY', sales=708, delivery='Free Delivery', picture = 'products/wall.jpg')
            Product.objects.create(product_id = 7, name='Barbie', price=34.9, store='Barbie Official', category='Toys/Kids', sales=2346, delivery='Free Delivery')
            Product.objects.create(product_id = 8, name='Lego', price=599.8, store='Lego Official', category='Toys/Kids', sales=609, delivery='Free Delivery')
            Product.objects.create(product_id = 9, name='Colored Pencil', price=5.9, store='Wood', category='Toys/Kids', sales=60235, delivery='Free Delivery')
            Product.objects.create(product_id = 10, name='Balloons', price=3.9, store='Amazon', category='Toys/Kids', sales=9905, delivery='Free Delivery')
            Product.objects.create(product_id = 11, name='Pokemon Cards', price=14.8, store='Pokemon', category='Toys/Kids', sales=17135, delivery='Free Delivery')
            Product.objects.create(product_id = 12, name='Cat Food', price=48.9, store='Poultry', category='Pets', sales=4135, delivery='Free Delivery')
            Product.objects.create(product_id = 13, name='Cat Litter', price=69.5, store='Poultry', category='Pets', sales=4135, delivery='Free Delivery')
            Product.objects.create(product_id = 14, name='Scratcher', price=20.5, store='Meowoou', category='Pets', sales=195, delivery='Free Delivery')
            Product.objects.create(product_id = 15, name='Dog Bark Collar', price=35.6, store='Dinjoo', category='Pets', sales=4097, delivery='Free Delivery')
            Product.objects.create(product_id = 16, name='Dog Bed', price=69.5, store='Amazon', category='Pets', sales=47, delivery='Free Delivery')
            Product.objects.create(product_id = 17, name='Sun Glasses', price=178.0, store='Ray-Ban', category='Fashion/Beauty', sales=415, delivery='Free Delivery')
            Product.objects.create(product_id = 18, name='Nacklaces', price=210.0, store='Pandora', category='Fashion/Beauty', sales=649, delivery='Free Delivery')
            Product.objects.create(product_id = 19, name='Tote Bag', price=24.8, store='The Drop', category='Fashion/Beauty', sales=2345, delivery='Free Delivery')
            Product.objects.create(product_id = 20, name='Highlighter', price=22.0, store='Glint', category='Fashion/Beauty', sales=22, delivery='Free Delivery')
            Product.objects.create(product_id = 21, name='Jacket', price=210.0, store='Amazon', category='Fashion/Beauty', sales=21458, delivery='Free Delivery')
            Product.objects.create(product_id = 22, name='Headphones', price=129.0, store='Beats', category='Electronics', sales=61758, delivery='Free Delivery')
            Product.objects.create(product_id = 23, name='Fast Charger', price=14.8, store='Amazon', category='Electronics', sales=1890, delivery='Free Delivery')
            Product.objects.create(product_id = 24, name='Coffee table', price=128.0, store='WLIVE', category='Home/DIY', sales=4563, delivery='Free Delivery')
            Product.objects.create(product_id = 25, name='Food Container', price=39.0, store='Amazon', category='Home/DIY', sales=558, delivery='Free Delivery')
        if not Warehouse.objects.exists():
            Warehouse.objects.create(whid = 1,x = 10, y=10)