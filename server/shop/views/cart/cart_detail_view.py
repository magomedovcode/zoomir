from drf_spectacular.utils import extend_schema
from shop.models import Cart
from shop.serializers import CartSerializer
from rest_framework import (
    generics,
    permissions
)


@extend_schema(tags=['Корзина'])
class CartDetailView(generics.RetrieveAPIView):
    """
    Получение корзины текущего пользователя
    """
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.prefetch_related(
            'products_in_carts__product_variant'
        ).select_related('user')

    def get_object(self):
        cart, created = self.get_queryset().get_or_create(user=self.request.user)
        return cart
