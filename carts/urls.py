from django.urls import path
from .views import CartAPIView, Cart, CartDetails,OrderAPIView

app_name = 'carts'

urlpatterns = [
    path('', Cart.as_view(), name='cart_api'),
    path('details', CartDetails.as_view(), name='cart_api'),
    path('cart', CartAPIView.as_view()),
    path('order', OrderAPIView.as_view()),
]
