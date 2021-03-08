from django.shortcuts import render, redirect, get_object_or_404
from . models import Product, Category, Cart, Review, CartItem

# Create your views here.


def index(request):

    products = Product.objects.all()
    context = {
        'products':products
    }

    return render(request, 'index.htm',context=context)

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)

    ctx = {
        'product':product
    }
    return render(request, 'product-detail.html', ctx)

def Add_to_cart(request, slug):
    # get the product
    product = get_object_or_404(Product, slug=slug)
    cart_product, created = CartItem.objects.get_or_create(user=request.user, product=product)
    cart_order, created = Cart.objects.get_or_create(user=request.user, number_of_products=20,total_amount=12)
    cart_order.products.add(cart_product)
    return redirect('/')
    # create an empty cart
    
def cart(request):
    cart = Cart.objects.get(user=request.user)
    context = {
        'cart':cart
    }
    return render(request, 'cart.html', context=context)
