from rest_framework import generics
from apps.categories.models import FishCategory
from .serializers import FCategorySerializer


class FCategoryListCreateView(generics.ListCreateAPIView):
    queryset = FishCategory.objects.all()
    serializer_class = FCategorySerializer


class FCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FishCategory.objects.all()
    serializer_class = FCategorySerializer
