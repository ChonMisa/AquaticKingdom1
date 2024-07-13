from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# from apps.fish.models import Fish
# from apps.fish_food.models import FishFood
# from apps.accessories.models import Accessory
from apps.cart.models import Cart, Order

from .serializers import CartSerializer, OrderSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    @method_decorator(login_required, name='dispatch')
    @action(detail=False, methods=['post'], url_path='purchase')
    def purchase_items(self, request):
        user = request.user
        cart = Cart.objects.get(user=user)
        if cart.items_cart.count() == 0:
            return Response({'error': 'Ваша корзина пуста.'}, status=status.HTTP_400_BAD_REQUEST)

        # Проверка наличия товаров на складе
        for item in cart.items_cart.all():
            if item.fish and item.fish.stock < item.quantity:
                restock_date = item.fish.restock_date or 'неизвестна'
                return Response({'error': f'Недостаточно товара: {item.fish.name}. Ожидаемая дата пополнения: {restock_date}'}, status=status.HTTP_400_BAD_REQUEST)
            if item.accessory and item.accessory.stock < item.quantity:
                restock_date = item.accessory.restock_date or 'неизвестна'
                return Response({'error': f'Недостаточно товара: {item.accessory.title}. Ожидаемая дата пополнения: {restock_date}'}, status=status.HTTP_400_BAD_REQUEST)
            if item.ffood and item.ffood.stock < item.quantity:
                restock_date = item.ffood.restock_date or 'неизвестна'
                return Response({'error': f'Недостаточно товара: {item.ffood.title}. Ожидаемая дата пополнения: {restock_date}'}, status=status.HTTP_400_BAD_REQUEST)

        # Создать заказ
        delivery_type = request.data.get('delivery_type')
        order = Order.objects.create(user=user, delivery_type=delivery_type)
        for item in cart.items_cart.all():
            order.items.add(item)
            # Уменьшить количество товара на складе
            if item.fish:
                item.fish.stock -= item.quantity
                item.fish.save()
            if item.accessory:
                item.accessory.stock -= item.quantity
                item.accessory.save()
            if item.ffood:
                item.ffood.stock -= item.quantity
                item.ffood.save()

        # Очистить корзину
        for item in cart.items_cart.all():
            item.delete()

        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# class ItemViewSet(viewsets.ModelViewSet):
#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer
#     permission_classes = [IsAuthenticated]
