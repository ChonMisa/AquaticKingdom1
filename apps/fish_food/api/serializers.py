from rest_framework import serializers
from apps.fish_food.models import FishFood


class FishFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = FishFood
        fields = '__all__'
