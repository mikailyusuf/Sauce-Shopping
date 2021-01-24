from django.db import models

from sauce_shopping.authentication.models import User
from sauce_shopping.products.models import Products


class ShippingAddress(models.Model):
    user = models.OneToOneField(User)
    country=models.CharField(max_length=255)
    postal_code=models.CharField(max_length=255,null=True)
    state=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    phone_number=models.CharField(max_length=255)


class Orders(models.Model):
    user = models.ForeignKey(User)
    product = models.ForeignKey(Products)
    date = models.DateTimeField(auto_created=True,auto_now_add=True)
    units= models.IntegerField(default=1)
    shipping_address = models.ForeignKey(ShippingAddress)