from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from .views import UploadProductView, ProductDetail

urlpatterns = [
    path('upload_product', UploadProductView.as_view(), name="upload-product"),
    path('product_detail/<int:pk>/', ProductDetail.as_view(), name="upload-product"),

]