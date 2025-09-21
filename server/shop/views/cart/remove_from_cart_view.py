from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from shop.models import ProductInCart
from shop.serializers import ProductInCartSerializer
from rest_framework import (
    generics,
    permissions,
    status
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

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
