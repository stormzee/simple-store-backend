from django.contrib import admin

# Register your models here.
from . models import User, Product, Review, Category, Cart

admin.site.register(User)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Category)
admin.site.register(Review)
