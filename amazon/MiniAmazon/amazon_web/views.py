from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Product, Cart, Order, OrderItem, Warehouse
from users.models import Profile
from django.contrib import messages
from django.db.models import F, Count, Avg
from django.db import transaction
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

def home(request):
    products = Product.objects.order_by('product_id')[:6] # Fetch the first 6 products
    return render(request, 'users/home.html', {'products': products})

@login_required
def search(request):
    name_query = request.GET.get('name')
    category_query = request.GET.get('category')
    min_price_query = request.GET.get('price-min')
    max_price_query = request.GET.get('price-max')
    sort_by = request.GET.get('sort-by')
    products = Product.objects.all()
    if name_query:
        products = products.filter(name__icontains=name_query)
    if category_query:
        products = products.filter(category=category_query)
    if min_price_query and max_price_query:
        products = products.filter(price__range=(min_price_query, max_price_query))
    elif min_price_query:
        products = products.filter(price__gte=min_price_query)
    elif max_price_query:
        products = products.filter(price__lte=max_price_query)
        
    avg_stars = {}
    for product in products:
        order_items = OrderItem.objects.filter(product=product)
        num_items = order_items.count()
        if num_items > 0:
            total_stars = sum([item.stars for item in order_items])
            avg_stars[product.product_id] = total_stars / num_items
        else:
            avg_stars[product.product_id] = 5.0
            
    if sort_by == 'price_asc':
        products = products.order_by('price')
    elif sort_by == 'price_desc':
        products = products.order_by('-price')
    elif sort_by == 'sales_asc':
        products = products.order_by('sales')
    elif sort_by == 'sales_desc':
        products = products.order_by('-sales')
    categories = Product.objects.values_list('category', flat=True).distinct()
    return render(request, 'amazon_web/search.html', {'products': products, 'categories': categories, 'avg_stars': avg_stars})

@login_required
def cart_view(request):
    cart = Cart.objects.filter(user=request.user)
    total_price = 0
    for item in cart:
        total_price += item.subtotal
    return render(request, 'amazon_web/cart.html', {'cart': cart, 'total_price': total_price})

@login_required
def delete_cart_item(request, item_id):
    cart_item = Cart.objects.get(id=item_id)
    cart_item.delete()
    messages.success(request, f"{cart_item.product.name} removed from cart!")
    return redirect('cart')


@transaction.atomic
def checkout(request):
    cart = Cart.objects.filter(user=request.user)
    for item in cart:
        Product.objects.filter(product_id=item.product.product_id).update(sales=F('sales') + item.quantity)
    total_price = sum([item.subtotal for item in cart])
    order = Order.objects.create(user=request.user, total_price=total_price, status='checked_out')
    for item in cart:
        order_item = OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity)
        order_item.save()
    order.save()
    cart.delete()
    profile = Profile.objects.get(user = request.user)
    profile.points += order.total_price*0.01
    profile.save()
    messages.success(request, "Checkout successful!")
    email = str(order.user.email)
    username = str(order.user.username)
    order_detail = str(order.__str__())
    send_confirmation_email(email, username, order_detail)
    return redirect('home') 


def view_completed_orders(request):
    orders = Order.objects.filter(user=request.user, status='delivered')
    if request.method == 'POST':
        order_item_id = request.POST.get('order_item_id')
        stars = request.POST.get('stars')
        try:
            order_item = OrderItem.objects.get(id=order_item_id, order__user=request.user)
            order_item.stars = stars
            order_item.save()
            messages.success(request, 'Rating submitted successfully.')
        except OrderItem.DoesNotExist:
            messages.error(request, 'Invalid order item ID.')
        return redirect('view_orders')
    return render(request, 'amazon_web/view_completed_orders.html', {'orders': orders})

def view_current_orders(request):
    orders = Order.objects.filter(user=request.user, status__in=['checked_out', 
                                                                'requesting_inventory', 
                                                                'inventory_arrived', 
                                                                'packing', 
                                                                'packed',
                                                                'booked_truck',
                                                                'truck_arrived',
                                                                'loading',
                                                                'loaded',
                                                                'delivering'])
    return render(request, 'amazon_web/view_current_orders.html', {'orders': orders})

@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(product_id=product_id)
    user = request.user
    quantity = int(request.POST.get('quantity{}'.format(product_id)))
    cart_item, created = Cart.objects.get_or_create(user=user, product=product)
    if not created:
        cart_item.quantity += quantity
        cart_item.save()
        messages.success(request, f"{quantity}x {product.name} added to cart!")
    else:
        cart_item.quantity = quantity
        cart_item.save()
        messages.success(request, f"{quantity}x {product.name} added to cart!")
    return redirect('search')

@login_required
def buy(request, product_id):
    product = Product.objects.get(product_id=product_id)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity{}'.format(product_id)))
        order = Order.objects.create(user=request.user, total_price=product.price)
        order_item = OrderItem.objects.create(order=order, product=product, quantity=quantity)
        order.total_price = order_item.quantity * product.price
        order.save()
        order_item.save()
        profile = Profile.objects.get(user = request.user)
        profile.points += order.total_price*0.01
        profile.save()
        messages.success(request, f"Successfully buy {quantity}x {product.name}")
        send_confirmation_email(request.user.email,request.user.username,order.__str__())
        return redirect('search')
    elif request.method == 'GET':
        quantity = int(request.GET.get('quantity{}'.format(product_id)))
        return render(request, 'confirm_purchase.html', {'product': product, 'quantity': quantity})

@login_required
def handle_cart(request, product_id):
    if request.method == 'POST':
        action = request.POST.get('action')
        quantity = int(request.POST.get('quantity', 1))
        product = Product.objects.get(product_id=product_id)
        user = request.user

        if action == 'buy':
            order = Order.objects.create(user=user, total_price=product.price)
            order_item = OrderItem.objects.create(order=order, product=product, quantity=quantity)
            order.total_price = order_item.quantity * product.price
            order.save()
            order_item.save()
            profile = Profile.objects.get(user = request.user)
            profile.points += order.total_price*0.01
            profile.save()
            messages.success(request, f"Successfully bought {quantity}x {product.name}")
            send_confirmation_email(request.user.email,request.user.username,order.__str__())
            return redirect('search')

        elif action == 'add_to_cart':
            cart_item, created = Cart.objects.get_or_create(user=user, product=product)
            if not created:
                cart_item.quantity += quantity
            else:
                cart_item.quantity = quantity
            cart_item.save()
            messages.success(request, f"{quantity}x {product.name} added to cart!")
            return redirect('search')

    return redirect('home')

@login_required
def rate_product(request, order_item_id):
    order_item = get_object_or_404(OrderItem, id=order_item_id)
    if request.method == 'POST':
        stars = request.POST.get('stars')
        if stars is not None:
            order_item.stars = int(stars)
            order_item.save()
            messages.success(request, f"Successfully rated {order_item.product.name}!")
            return redirect('view_completed_orders')
    return render(request, 'amazon_web/rate_product.html', {'order_item': order_item})


def send_confirmation_email(user_email, user_name,request_details):
    subject = 'Order Placed'
    message = 'Dear '+ user_name +',\n\nYour order has been successfully placed!\n\nDetails:\n' + request_details + '\n\nYour items will be shipped soon.\n\nBest regards,\nAmazon'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user_email]
    send_mail(subject, message, email_from, recipient_list)