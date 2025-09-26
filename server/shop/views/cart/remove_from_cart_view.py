from drf_spectacular.utils import extend_schema
from shop.models import ProductInCart
from shop.serializers import ProductInCartSerializer
from rest_framework import (
    generics,
    permissions
)


@extend_schema(tags=['Корзина'])
class RemoveFromCartView(generics.DestroyAPIView):
    """
    Удаление товара из корзины
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProductInCartSerializer

    def get_queryset(self):
        return ProductInCart.objects.filter(cart__user=self.request.user)
