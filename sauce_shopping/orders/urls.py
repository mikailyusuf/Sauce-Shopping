from django.urls import path

from orders.views import CreateOrderView, OrdersDetailsView, ShippingAdressView, CartView

urlpatterns = [
    path('create_order', CreateOrderView.as_view(), name="create_order"),
    path('order_details/<int:pk>/', OrdersDetailsView.as_view(), name="order_details"),

    path('shipping_address', ShippingAdressView.as_view(), name="shipping_address"),
    path('cart', CartView.as_view(), name="cart"),

]