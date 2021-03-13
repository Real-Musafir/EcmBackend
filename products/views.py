from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer
from rest_framework import viewsets, filters, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView



class ProductList(generics.ListAPIView):

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
