from rest_framework import serializers
from apps.cart.models import Cart, Item
from apps.fish.models import Fish
from apps.accessories.models import Accessory
from apps.fish_food.models import FishFood


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'fish', 'accessory', 'ffood', 'quantity', 'cart']


class CartSerializer(serializers.ModelSerializer):
    items_cart = ItemSerializer(many=True, read_only=True)
    total_sum = serializers.ReadOnlyField(source='get_total_sum')

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items_cart', 'total_sum']
