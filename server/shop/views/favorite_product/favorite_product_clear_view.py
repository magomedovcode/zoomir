from drf_spectacular.utils import extend_schema
from rest_framework import (
    generics,
    permissions
)
from shop.models import FavoriteProduct
from shop.serializers import FavoriteProductSerializer


@extend_schema(tags=['Избранное'])
class FavoriteProductClearView(generics.DestroyAPIView):
    """
    Удаление всех товаров из избранного текущего пользователя
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FavoriteProductSerializer

    def get_queryset(self):
        return FavoriteProduct.objects.filter(user=self.request.user)
