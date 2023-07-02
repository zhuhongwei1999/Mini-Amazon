from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart'),
    path('delete_cart_item/<int:item_id>/', views.delete_cart_item, name='delete_cart_item'),
    path('checkout/', views.checkout, name='checkout'),
    path('buy/<int:product_id>/', views.buy, name='buy'),
    path('handle_cart/<int:product_id>/', views.handle_cart, name='handle_cart'),
    path('view_current_orders/', views.view_current_orders, name='view_current_orders'),
    path('view_completed_orders/', views.view_completed_orders, name='view_completed_orders'),
    path('rate_product/<int:order_item_id>/', views.rate_product, name='rate_product'),
]