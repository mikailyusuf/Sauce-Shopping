from django.db import models

from authentication.models import User


class Products(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=250, null=False)
    product_description = models.TextField(max_length=250, null=False)
    max_delivery_time = models.CharField(max_length=250, null=False,default="1 Week")
    product_photo = models.ImageField()
    price = models.DecimalField(max_digits=50, decimal_places=2)
    date_created = models.DateField(auto_created=True, auto_now=True)
