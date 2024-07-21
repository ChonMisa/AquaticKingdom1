from django.urls import path
from .views import FishCategoryListView

urlpatterns = [
    path('categories/', FishCategoryListView.as_view(), name='fish_category_list'),
]