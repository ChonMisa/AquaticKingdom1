from rest_framework import serializers
from apps.fish_food.models import FishFood, FishFoodImage


class FfoodImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FishFoodImage
        fields = '__all__'

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None


class FishFoodSerializer(serializers.ModelSerializer):
    ffood_images = FfoodImageSerializer(many=True, read_only=True)

    class Meta:
        model = FishFood
        fields = '__all__'
