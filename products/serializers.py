from rest_framework import serializers
from .models import Product
from django.conf import settings


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'image', 'description', 'price', 'slug']
