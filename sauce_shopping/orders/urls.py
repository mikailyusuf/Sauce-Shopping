from django.urls import path

from sauce_shopping.orders.views import CreateOrderView, OrdersDetailsView, ShippingAdressView

urlpatterns = [
    path('create_order', CreateOrderView.as_view(), name="create_order"),
    path('order_details', OrdersDetailsView.as_view(), name="order_details"),


    path('shipping_address', ShippingAdressView.as_view(), name="order_details"),

]