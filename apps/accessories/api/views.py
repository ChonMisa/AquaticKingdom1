from rest_framework import generics
from apps.accessories.models import Accessory
from .serializers import AccessorySerializer


class AccessoryListCreateView(generics.ListCreateAPIView):
    queryset = Accessory.objects.all()
    serializer_class = AccessorySerializer


class AccessoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Accessory.objects.all()
    serializer_class = AccessorySerializer
