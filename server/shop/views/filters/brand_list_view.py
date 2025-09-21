from drf_spectacular.utils import extend_schema
from shop.models import Brand
from shop.serializers import BrandSerializer
from rest_framework import (
    generics,
    permissions
)


@extend_schema(tags=['Бренды'])
class BrandListView(generics.ListAPIView):
    """
    Получение списка всех брендов
    """
    serializer_class = BrandSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Brand.objects.all()
