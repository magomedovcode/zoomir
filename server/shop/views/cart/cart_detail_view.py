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

    def get_object(self):
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        return cart
