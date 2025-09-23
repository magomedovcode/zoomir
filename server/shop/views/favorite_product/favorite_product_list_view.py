from drf_spectacular.utils import extend_schema
from shop.models import FavoriteProduct
from shop.pagination import Pagination
from shop.serializers import FavoriteProductSerializer
from rest_framework import (
    generics,
    permissions
)


@extend_schema(tags=['Избранное'])
class FavoriteProductListView(generics.ListAPIView):
    """
    Список избранных товаров текущего пользователя
    """
    serializer_class = FavoriteProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = Pagination

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return FavoriteProduct.objects.none()

        return FavoriteProduct.objects.filter(
            user=self.request.user
        ).select_related(
            'product__brand',
            'product__country'
        )
