from django.db import models

from sauce_shopping.authentication.models import User


class Image(models.Model):
    image = models.ImageField(blank=True, null=True, upload_to='images')


class Products(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=250, null=False)
    product_description = models.TextField(max_length=250, null=False)
    max_delivery_time = models.CharField(max_length=250, null=False, default="1 Week")
    images = models.JSONField(null=True)
    units_available = models.IntegerField()
    price = models.DecimalField(max_digits=50, decimal_places=2)
    date_created = models.DateField(auto_created=True, auto_now=True)

    def __str__(self):
        return self.product_name


