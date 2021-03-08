from django.contrib import admin

# Register your models here.
from . models import User, Product, Review, Category, Cart, CartItem

admin.site.register(User)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Category)
admin.site.register(Review)
admin.site.register(CartItem)