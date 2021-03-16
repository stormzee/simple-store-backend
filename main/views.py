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

    if cart_product:
        cart_product.quantity += 1
    cart_product.save()

    cart_order, created = Cart.objects.get_or_create(user=request.user)
    cart_order.products.add(cart_product)
    cart_order.number_of_products = cart_order.products.count()
    qs = cart_order.products.all()

    if qs.exists():
        for item in qs:
            cart_order.total_amount += item.product.price
    
    cart_order.save()
    return redirect('/')
    # create an empty cart
    
def cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_products = cart.products.all()
    context = {
        'cart_products':cart_products
    }
    return render(request, 'cart.html', context=context)


def remove_from_cart(request, cart_item_id):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item = cart.products.get(product=cart_item_id)
    cart.products.remove(cart_item)
    cart.save()
    return redirect('cart')
