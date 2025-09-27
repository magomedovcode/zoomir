from drf_spectacular.utils import extend_schema
from rest_framework import (
    generics,
    permissions,
    status
)
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from shop.models import ProductInCart, Cart
from shop.serializers.cart_content.update_cart_serializer import UpdateCartItemSerializer


@extend_schema(
    tags=['Корзина'],
    request=UpdateCartItemSerializer,
    responses={200: UpdateCartItemSerializer}
)
class UpdateCartView(generics.UpdateAPIView):
    """
    Обновление количества товара в корзине
    """
    serializer_class = UpdateCartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

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

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data, status=status.HTTP_200_OK)
