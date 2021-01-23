import jwt
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render
from django.urls import reverse
from rest_framework import generics, status, views, permissions, viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Products, Image
from .serializers import ProductSerializer, ImageSerializer
from . import utils
from .utils import Utils


class TestUpload(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    parser_classes = (MultiPartParser, FormParser)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()


class UploadProductView(generics.GenericAPIView):
    # queryset = Products.objects.all()
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        product_name = request.data['product_name']
        product_description = request.data['product_description']
        max_delivery_time = request.data['max_delivery_time']
        units_available = request.data['units_available']
        price = request.data['price']
        flag = 1
        images = []
        files = request.FILES.getlist('images')
        for file in files:
            modified_data = Utils.modify_input_for_multiple_files(file)
            file_serializer = ImageSerializer(data=modified_data)
            if file_serializer.is_valid():
                file_serializer.save()
                images.append(file_serializer.data)
            else:
                flag = 0

        if flag == 1:
            try:
                product = Products.objects.create(product_name=product_name, product_description=product_description,
                                                  price=price, max_delivery_time=max_delivery_time,
                                                  images=images, units_available=units_available)
            except:
                error = {'error': 'An error occured when registering the products'}

                return Response(error, status=status.HTTP_403_FORBIDDEN, )

            serializer = ProductSerializer(product)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            error = {'error': 'An error occured when registering the products'}
            return Response(error, status=status.HTTP_400_BAD_REQUEST)
