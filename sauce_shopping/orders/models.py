from django.db import models

from authentication.models import User
from products.models import Products


class ShippingAddress(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    country=models.CharField(max_length=255)
    postal_code=models.CharField(max_length=255,null=True)
    state=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    phone_number=models.CharField(max_length=255)


class Orders(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_created=True,auto_now_add=True)
    units= models.IntegerField(default=1)
    shipping_address = models.ForeignKey(ShippingAddress,on_delete=models.CASCADE)