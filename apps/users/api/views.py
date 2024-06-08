from rest_framework import generics
from apps.users.models import CustomUser
from .serializers import CustomUserSerializer, CustomUserCreateSerializer
from rest_framework.permissions import IsAuthenticated


class CustomUserListView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CustomUserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]


class CustomUserCreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserCreateSerializer
