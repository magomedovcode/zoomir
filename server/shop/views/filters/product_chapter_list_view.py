from drf_spectacular.utils import extend_schema
from shop.models import ProductChapter
from shop.serializers import ProductChapterSerializer
from rest_framework import (
    generics,
    permissions
)


@extend_schema(tags=['Главы категорий товаров'])
class ProductChapterListView(generics.ListAPIView):
    """
    Получение списка всех глав категорий товаров
    """
    serializer_class = ProductChapterSerializer
    permission_classes = [permissions.AllowAny]
    queryset = ProductChapter.objects.all()
