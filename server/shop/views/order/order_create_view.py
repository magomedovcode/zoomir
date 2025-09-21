from drf_spectacular.utils import extend_schema
from shop.serializers import OrderCreateSerializer
from rest_framework import (
    permissions,
    generics
)


@extend_schema(tags=['Заказы'], request=OrderCreateSerializer)
class OrderCreateView(generics.CreateAPIView):
    """
    Создание нового заказа
    """
    serializer_class = OrderCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
