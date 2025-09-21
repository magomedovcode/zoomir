from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.types import OpenApiTypes
from rest_framework import generics, permissions
from shop.filters import ProductVariantFilter
from shop.models import ProductVariant
from shop.pagination import ProductPagination
from shop.serializers import ProductVariantListSerializer
from drf_spectacular.utils import (
    extend_schema,
    OpenApiParameter
)


@extend_schema(
    tags=['Список товаров'],
    parameters=[
        OpenApiParameter(
            name='brand',
            description='Фильтр по ID бренда',
            required=False,
            type=OpenApiTypes.INT
        ),
        OpenApiParameter(
            name='product_category',
            description='Фильтр по ID категории товара',
            required=False,
            type=OpenApiTypes.INT
        ),
        OpenApiParameter(
            name='country',
            description='Фильтр по ID страны',
            required=False,
            type=OpenApiTypes.INT
        ),
        OpenApiParameter(
            name='search',
            description='Поиск по названию и описанию товара',
            required=False,
            type=OpenApiTypes.STR
        ),
        OpenApiParameter(
            name='ordering',
            description='Сортировка результатов (price, -price)',
            required=False,
            type=OpenApiTypes.STR
        ),
    ]
)
class ProductListView(generics.ListAPIView):
    """
    Получение списка всех вариаций продукта с фильтрацией
    """
    serializer_class = ProductVariantListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductVariantFilter
    permission_classes = [permissions.AllowAny]
    pagination_class = ProductPagination
    ordering_fields = ['price']
    ordering = ['id']

    queryset = ProductVariant.objects.select_related(
        'product',
        'product__brand',
        'product__country',
        'product__product_category'
    ).prefetch_related(
        'product_images',
        'attributes',
        'attributes__attribute_category'
    ).all()
