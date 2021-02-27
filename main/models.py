from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    pass


class Category(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    number_of_products = models.PositiveIntegerField(default=0)
    slug = models.SlugField()

    def __str__(self):
        return '%s %s'%(self.title, self.number_of_products)
    

class Product(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    price = models.FloatField(null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='', null=False, blank=False)
    category = models.ManyToManyField(Category, null=False, blank=False)
    slug = models.SlugField()
    item_count = models.PositiveIntegerField(default=1)
    time_created = models.DateTimeField(auto_now=True)
    in_stock = models.BooleanField()

    def is_available(self):
        if self.item_count == 0:
            self.in_stock = True
        return self.in_stock

    def save(self, *args, **kwargs):
        self.is_available()
        super(Product).save(*args, **kwargs)
    
    def __str__(self):
            return '%s - %s'%(self.name, self.price)


class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    number_of_products = models.PositiveIntegerField(default=0)
    total_amount = models.FloatField()

    def __str__(self):
        return "%s's cart"%(self.user.username)
    

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.TextField(max_length=500)
    rating = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "%s's review on %s"%(self.user.username, self.product)
    