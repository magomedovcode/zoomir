from drf_spectacular.utils import extend_schema
from rest_framework.generics import get_object_or_404

from shop.models import ProductInCart, Cart
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

    def get_object(self):
        product_variant_id = self.kwargs.get('product_variant_id')

        cart = get_object_or_404(Cart, user=self.request.user)

        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            product_variant_id=product_variant_id,
            cart=cart
        )
        return obj
