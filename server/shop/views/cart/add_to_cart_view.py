from drf_spectacular.utils import extend_schema
from shop.serializers import ProductInCartCreateSerializer
from rest_framework import (
    generics,
    permissions
)


@extend_schema(tags=['Корзина'], request=ProductInCartCreateSerializer)
class AddToCartView(generics.CreateAPIView):
    """
    Добавление товара в корзину
    """
    serializer_class = ProductInCartCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
