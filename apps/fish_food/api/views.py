from rest_framework import generics
from apps.fish_food.models import FishFood
from apps.fish_food.api.serializers import FishFoodSerializer


class FishFoodListCreateView(generics.ListCreateAPIView):
    queryset = FishFood.objects.all()
    serializer_class = FishFoodSerializer


class FishFoodDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FishFood.objects.all()
    serializer_class = FishFoodSerializer

