from drf_spectacular.utils import extend_schema
from rest_framework.generics import get_object_or_404
from shop.models import FavoriteProduct
from shop.serializers import FavoriteProductSerializer
from rest_framework import (
    generics,
    permissions
)


@extend_schema(tags=['Избранное'])
class FavoriteProductDeleteView(generics.DestroyAPIView):
    """
    Удаление товара из избранного
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FavoriteProductSerializer

    def get_queryset(self):
        return FavoriteProduct.objects.filter(user=self.request.user)

    def get_object(self):
        product_id = self.kwargs.get('product_id')

        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, product_id=product_id)
        return obj
