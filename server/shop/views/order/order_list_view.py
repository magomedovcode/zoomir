from drf_spectacular.utils import extend_schema
from shop.models import Order
from shop.serializers import OrderSerializer
from rest_framework import (
    generics,
    permissions
)


@extend_schema(tags=['Заказы'])
class OrderListView(generics.ListAPIView):
    """
    Список заказов текущего пользователя
    """
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Order.objects.none()

        return Order.objects.filter(
            user=self.request.user
        ).prefetch_related(
            'products_in_orders__product_variant__product'
        )
