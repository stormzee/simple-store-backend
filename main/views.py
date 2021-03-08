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
    cart_product = CartItem.objects.get_or_create(product=product.id, user=request.user)
    cart_order, created = Cart.objects.get_or_create(user=request.user, products=cart_product, total_amount=20.3)
    cart_order.save()
    return redirect('/')
    # create an empty cart
    
def cart(request):
    cart = Cart.objects.get(user=request.user)
    context = {
        'cart':cart
    }
    return render(request, 'cart.html', context=context)
