from django.http import Http404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, permissions, generics
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Products
from .serializers import ProductSerializer, ImageSerializer
from .utils import Utils


class ProductDetail(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ProductSerializer

    def get_object(self, pk):
        try:
            return Products.objects.get(pk=pk)
        except Products.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        products = self.get_object(pk)
        serializer = ProductSerializer(products)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # def put(self, request, pk, format=None):
    #     snippet = self.get_object(pk)
    #     serializer = ProductSerializer(snippet, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        if(request.user.is_staff):
            product = self.get_object(pk)
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class UploadProductView(generics.GenericAPIView):
    serializer_class = ProductSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = (permissions.IsAuthenticated,)


    @swagger_auto_schema(operation_description='Upload file...',)
    @action(detail=False, methods=['post'])
    def post(self, request):
        user = request.user
        product_name = request.data['product_name']
        product_description = request.data['product_description']
        max_delivery_time = request.data['max_delivery_time']
        category = request.data['category']
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
                product = Products.objects.create(user=user, product_name=product_name,category=category,
                                                  product_description=product_description,
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
