from django.urls import path
from .views import FCategoryListCreateView, FCategoryDetailView

urlpatterns = [
    path('categories/', FCategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', FCategoryDetailView.as_view(), name='category-detail'),
]
