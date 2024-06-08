from rest_framework import generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from apps.fish.models import Fish, FishImage
from .serializers import FishSerializer, FishImageSerializer
#
#


class FishViewSet(viewsets.ModelViewSet):
    queryset = Fish.objects.all()
    serializer_class = FishSerializer
#
#
# class FishCreateAPIView(generics.CreateAPIView):
#     queryset = Fish.objects.all()
#     serializer_class = FishSerializer
#
#
# class FishImageCreateAPIView(generics.ListCreateAPIView):
#     queryset = FishImage.objects.all()
#     serializer_class = FishImageSerializer
#
#
# class FishUpdateDeleteRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Fish.objects.all()
#     serializer_class = FishImageSerializer
#
#
# class FishImageUpdateDeleteRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = FishImage.objects.all()
#     serializer_class = FishImageSerializer
#
