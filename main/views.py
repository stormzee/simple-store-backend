from django.shortcuts import render, redirect, get_object_or_404
from . models import Product, Category, Cart, Review

# Create your views here.


def index(request):

    products = Product.objects.all()
    context = {
        'products':products
    }

    return render(request, 'index.htm',context=context)

def Add_to_cart(request, slug):
    # get the product
    product = get_object_or_404(Product, slug=slug)
    # create an empty cart
    new_cart = Cart.objects.get_or_create(user=request.user)
    new_cart.products.add(product, bulk=False)
    new_cart.number_of_products  = 0
    new_cart.total_amount = 30.0
    new_cart.save()
    return redirect('/')

def cart(request):
    cart = Cart.objects.get(user=request.user)
    context = {
        'cart':cart
    }
    return render(request, 'cart.html', context=context)
