
from django.urls import path
from . views import index, Add_to_cart, cart, product_detail

urlpatterns = [
    path('', index, name='index'),
    path('add-to-cart/<str:slug>/', Add_to_cart, name='add-to-cart'),
    path('product-detail/<str:slug>/', product_detail, name='product-detail'),
    path('cart/', cart, name='cart'),
]
