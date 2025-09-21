from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from shop.models import FavoriteProduct
from shop.serializers import FavoriteProductSerializer
from rest_framework import (
    generics,
    permissions,
    status
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

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
