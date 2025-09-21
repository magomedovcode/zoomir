from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.types import OpenApiTypes
from shop.models import ProductCategory
from shop.serializers import ProductCategorySerializer
from drf_spectacular.utils import (
    extend_schema,
    OpenApiParameter
)
from rest_framework import (
    generics,
    permissions
)


@extend_schema(
    tags=['Категории товаров'],
    parameters=[
        OpenApiParameter(
            name='product_chapter',
            description='Фильтр по главе категорий товара (ID)',
            required=False,
            type=OpenApiTypes.INT
        )
    ]
)
class ProductCategoryListView(generics.ListAPIView):
    """
    Получение списка всех категорий товаров
    """
    serializer_class = ProductCategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['product_chapter', ]
    permission_classes = [permissions.AllowAny]
    queryset = ProductCategory.objects.select_related(
        'product_chapter'
    ).all()
