
from django.urls import path
from . views import index, Add_to_cart, cart

urlpatterns = [
    path('', index, name='index'),
    path('add-product/<str:slug>/', Add_to_cart, name='add-to-cart'),
    path('cart', cart, name='cart'),
]
