from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from .views import TestUpload, UploadProductView

router = routers.DefaultRouter()
router.register('', TestUpload, basename='cutareadel')

urlpatterns = [
# url('upload_product', include(router.urls)),
    path('upload_product', UploadProductView.as_view(), name="upload-product"),
    # path('email-verify/', VerifyEmail.as_view(), name="email-verify"),
    # path('login/', LoginAPIView.as_view(), name="login"),
    # path('logout/', LogoutAPIView.as_view(), name="logout"),

]