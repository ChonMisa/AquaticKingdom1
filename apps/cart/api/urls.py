from django.urls import path
from .views import CartListView, CartDetailView, ItemListView, ItemDetailView

urlpatterns = [
    path('carts/', CartListView.as_view(), name='cart-list'),
    path('carts/<int:pk>/', CartDetailView.as_view(), name='cart-detail'),
    path('items/', ItemListView.as_view(), name='item-list'),
    path('items/<int:pk>/', ItemDetailView.as_view(), name='item-detail'),
]
