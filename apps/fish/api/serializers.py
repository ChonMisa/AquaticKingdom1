from rest_framework import serializers

from apps.fish.models import Fish, FishImage


class FishImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FishImage
        fields = '__all__'


class FishSerializer(serializers.ModelSerializer):
    fish_images = FishImageSerializer(many=True, read_only=True)

    class Meta:
        model = Fish
        fields = '__all__'
