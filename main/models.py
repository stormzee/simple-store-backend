from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.urls import reverse


class User(AbstractUser):
    pass


class Category(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return '%s'%(self.title)

    class Meta:
        verbose_name_plural = 'Categories'
    

class Product(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    price = models.FloatField(null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='', null=False, blank=False)
    category = models.ManyToManyField(Category)
    slug = models.SlugField(unique=True)
    item_count = models.PositiveIntegerField(default=1)
    time_created = models.DateTimeField(auto_now=True)
    in_stock = models.BooleanField()


    def is_available(self):
        if self.item_count == 0:
            self.in_stock = True
        return self.in_stock

    def save(self, *args, **kwargs):
        self.is_available()
        super().save(*args, **kwargs)

    # def get_absolute_url(self):
    #     return reverse("Product.slug", kwargs={"pk": self.pk})
    
    
    def __str__(self):
            return '%s - %s'%(self.name, self.price)

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.product.name

class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    products = models.ManyToManyField(CartItem)
    number_of_products = models.PositiveIntegerField(default=0)
    total_amount = models.FloatField()


    # def get_absolute_url(self):
    #     return reverse("Cart.user.username", kwargs={"pk": self.pk})
    

    def __str__(self):
        return "%s's cart"%(self.user.username)
    

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.TextField(max_length=500)
    rating = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "%s's review on %s"%(self.user.username, self.product)

    # def get_absolute_url(self):
    #     return reverse("Review.user.username", kwargs={"pk": self.pk})
    
    