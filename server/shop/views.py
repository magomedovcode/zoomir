from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import permissions, generics
from rest_framework.filters import SearchFilter
from shop.pagination import ProductPagination
from shop.filters import ProductVariantFilter
from shop.models import (
    Brand,
    Country,
    ProductChapter,
    ProductCategory,
    ProductVariant
)
from shop.serializers import (
    BrandSerializer,
    CountrySerializer,
    ProductChapterSerializer,
    ProductCategorySerializer,
    ProductVariantSerializer
)


@extend_schema(tags=['Главы категорий продуктов'])
class ProductChapterListView(generics.ListAPIView):
    """
    Получение списка всех глав категорий продуктов
    """
    queryset = ProductChapter.objects.all()
    serializer_class = ProductChapterSerializer
    pagination_class = None
    permission_classes = [permissions.AllowAny]


@extend_schema(
    tags=['Категории продукта'],
    parameters=[
        OpenApiParameter(
            name='product_chapter',
            description='Фильтр по главе категорий продукта (ID)',
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
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['product_chapter', ]
    pagination_class = None
    permission_classes = [permissions.AllowAny]
    queryset = ProductCategory.objects.select_related('product_chapter').all()


@extend_schema(tags=['Бренды'])
class BrandListView(generics.ListAPIView):
    """
    Получение списка всех брендов
    """
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    pagination_class = None
    permission_classes = [permissions.AllowAny]


@extend_schema(tags=['Страны производства'])
class CountryListView(generics.ListAPIView):
    """
    Получение списка всех стран производителей
    """
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    pagination_class = None
    permission_classes = [permissions.AllowAny]


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
            name='attribute_category',
            description='Фильтр по ID категории атрибута',
            required=False,
            type=OpenApiTypes.INT
        ),
        OpenApiParameter(
            name='search',
            description='Поиск по названию и описанию товара',
            required=False,
            type=OpenApiTypes.STR
        ),
    ]
)
class ProductListView(generics.ListAPIView):
    """
    Получение списка всех вариаций продукта с фильтрацией
    """
    serializer_class = ProductVariantSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = ProductVariantFilter
    permission_classes = [permissions.AllowAny]
    pagination_class = ProductPagination
    ordering_fields = ['price']

    queryset = ProductVariant.objects.select_related(
        'product',
        'product__brand',
        'product__country',
        'product__product_category'
    ).prefetch_related(
        'product_images',
        'attributes',
        'attributes__attribute_category',
        'product__tags'
    ).all()
