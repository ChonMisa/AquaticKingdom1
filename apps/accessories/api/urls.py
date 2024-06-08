from django.urls import path
from .views import AccessoryListCreateView, AccessoryDetailView

urlpatterns = [
    path('accessories/', AccessoryListCreateView.as_view(), name='accessory-list-create'),
    path('accessories/<int:pk>/', AccessoryDetailView.as_view(), name='accessory-detail'),
]
