from django.http import Http404
from django.shortcuts import render
from requests import Response
from rest_framework import status, permissions
from rest_framework.views import APIView

from sauce_shopping.orders.models import Orders, ShippingAddress
from sauce_shopping.orders.serializers import OrdersSerializer, ShippingAdrressSerializer


class OrdersDetailsView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Orders.objects.get(pk=pk)
        except Orders.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = OrdersSerializer(snippet)
        return Response(serializer.data)

    # def put(self, request, pk, format=None):
    #     snippet = self.get_object(pk)
    #     serializer = OrdersSerializer(snippet, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CreateOrderView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        user = request.user
        product = request.data['product']
        units = request.data['units']
        shipping_address = request.data['shipping_address']
        Orders.objects.create(user=user, product=product, units=units, shipping_address=shipping_address)


class ShippingAdressView(APIView):

    def post(self, request):
        user = request.user
        country = request.data['country']
        state = request.data['state']
        address = request.data['address']
        phone_number = request.data['phone_number']
        order = ShippingAddress.objects.create(user=user, country=country, state=state,
                                               address=address, phone_number=phone_number)
        serializer = ShippingAdrressSerializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request, pk, format=None):
        user = request.user
        try:
            address = ShippingAddress.objects.filter(user=user)
            serializer = ShippingAdrressSerializer(address)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except ShippingAddress.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        user = request.user
        address = ShippingAddress.objects.filter(user=user)
        address.delete
        serializer = ShippingAdrressSerializer(address)
        return Response(serializer.data, status=status.HTTP_200_OK)




