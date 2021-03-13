
from rest_framework import serializers


from .models import CartItem, Cart
from .mixins import TokenMixin




class CartItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = ('cart','item','quantity', 'line_item_total')

class CartItems(serializers.ModelSerializer):
    item_title = serializers.SerializerMethodField()
    class Meta:
        model = CartItem
        fields = ('cart','item','item_title','quantity', 'line_item_total')
        
    def get_item_title(self, obj):
        return "%s" %(obj.item.title)
        

class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = [
            'id',
            'user',
            'total',
            'active',
            'ordered'
        ]
