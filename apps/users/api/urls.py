from django.urls import path
from .views import CustomUserListView, CustomUserDetailView, CustomUserCreateView

urlpatterns = [
    path('users/', CustomUserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', CustomUserDetailView.as_view(), name='user-detail'),
    path('users/create/', CustomUserCreateView.as_view(), name='user-create'),
]
