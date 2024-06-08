from django.urls import path
from .views import FishFoodListCreateView, FishFoodDetailView

urlpatterns = [
    path('fishfoods/', FishFoodListCreateView.as_view(), name='fishfood-list-create'),
    path('fishfoods/<int:pk>/', FishFoodDetailView.as_view(), name='fishfood-detail'),
]
