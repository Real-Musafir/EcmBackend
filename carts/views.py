from django.shortcuts import render
from .models import Cart, CartItem
from rest_framework.response import Response
from .mixins import TokenMixin, CartUpdateAPIMixin, CartTokenMixin
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .serializers import CartItemSerializer, CartSerializer, CartItems
from .permissions import IsOwnerOrReadOnly
from .models import Cart as CartModel
from products.models import Product
from django.shortcuts import get_object_or_404


from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    UpdateAPIView,
    DestroyAPIView,
    RetrieveDestroyAPIView,
)

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
    BasePermission
)

class Cart(ListAPIView):
	serializer_class = CartItems

	def get_cart(self):
		user = self.request.user
		try:
			cart = CartModel.objects.get(user = user, active=True, ordered=False)
		except:
			cart = CartModel()
			cart.user = user
			cart.save()
		return cart

	def get_queryset(self):
		cart = self.get_cart()
		queryset1 = CartItem.objects.filter(cart=cart)
		return queryset1

class CartDetails(APIView):
	queryset = CartItem.objects.all()

	def get_cart(self):
		user = self.request.user
		try:
			cart = CartModel.objects.get(user = user, active=True, ordered=False)
		except:
			cart = CartModel()
			cart.user = user
			cart.save()
		return cart

	def post(self, request, format=None):
		cart = self.get_cart()

		data = request.data
		item_id = data["item"]
		qty = data["quantity"]
		# qty = 0
		if item_id:
			item_instance = get_object_or_404(Product, id=item_id)
			print("Cart is: ", cart, "Itme is: ", item_instance)
			
			
			try:
				cart_item = CartItem.objects.get(cart=cart, item=item_instance)
				
				if int(qty) == 0:
					print(qty, "Yes i am here")
					cart_item.delete()
				else:
					print(cart_item.quantity, "This is quantity")
					cart_item.quantity = int(qty) + int(cart_item.quantity)
					cart_item.save()
			except:
				cart_item = CartItem.objects.create(cart=cart, item=item_instance, quantity=int(qty))
			
			return Response("EVERYTHING OK")
		else:
			return Response("SOMETHING WRONG")	
			
			return Response(data)



class CartAPIView(ListAPIView):
	serializer_class = CartSerializer

	def get_queryset(self, *args, **kwargs):
		user = self.request.user
		queryset_list = CartModel.objects.filter(user=user, active=True, ordered=False)
		return queryset_list

class OrderAPIView(ListAPIView):
	print("Ordered .............................")
	serializer_class = CartSerializer

	def get_queryset(self, *args, **kwargs):
		user = self.request.user
		try:
			print("Try To Find .......................")
			queryset_list = CartModel.objects.get(user=user, active=True, ordered=False)
			print(queryset_list.ordered,"Fing--------------------------")
			queryset_list.ordered = True
			print(queryset_list.ordered, "What is this")
			queryset_list.save()
		except:
			queryset_list = None
		return queryset_list


