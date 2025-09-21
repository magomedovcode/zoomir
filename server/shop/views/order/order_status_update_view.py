from drf_spectacular.utils import extend_schema
from shop.models import Order
from shop.serializers import OrderStatusUpdateSerializer
from rest_framework import (
    generics,
    permissions
)


@extend_schema(tags=['Заказы'], request=OrderStatusUpdateSerializer)
class OrderStatusUpdateView(generics.UpdateAPIView):
    """
    Обновление статуса заказа (только для администраторов)
    """
    serializer_class = OrderStatusUpdateSerializer
    permission_classes = [permissions.IsAdminUser]
    queryset = Order.objects.all()
