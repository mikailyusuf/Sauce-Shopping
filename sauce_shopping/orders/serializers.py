from rest_framework import serializers

from authentication.models import User
from orders.models import ShippingAddress, Orders, Cart


class ShippingAdrressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]


class OrdersSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Orders
        fields = ["user", "product"]
        depth = 1


class CartSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Cart
        fields = ["user", "product"]
        depth = 1
