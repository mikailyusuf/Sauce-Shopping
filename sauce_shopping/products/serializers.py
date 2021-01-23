from rest_framework import serializers
from .models import Products, Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'
