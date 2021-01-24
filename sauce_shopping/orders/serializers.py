from rest_framework import serializers

from sauce_shopping.orders.models import ShippingAdrress, Orders


class ShippingAdrressSerializer(serializers.ModelSerializer):
    class Meta:
        Model = ShippingAdrress
        fields = '__all__'


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        Model = Orders
        fields = '__all__'
