import django_filters
from django.db import models
from shop.models import (
    ProductVariant,
    ProductCategory
)


class ProductVariantFilter(django_filters.FilterSet):
    brand = django_filters.BaseInFilter(field_name='product__brand_id')
    product_category = django_filters.BaseInFilter(field_name='product__product_category_id')
    country = django_filters.BaseInFilter(field_name='product__country_id')
    search = django_filters.CharFilter(method='filter_search')
    price = django_filters.RangeFilter(field_name='price')

    @staticmethod
    def filter_search(queryset, name, value):
        return queryset.filter(
            models.Q(product__title__icontains=value) |
            models.Q(product__description__icontains=value)
        )

    class Meta:
        model = ProductVariant
        fields = []


class ProductCategoryFilter(django_filters.FilterSet):
    product_chapter = django_filters.BaseInFilter(field_name='product_chapter__id', lookup_expr='in')

    class Meta:
        model = ProductCategory
        fields = ['product_chapter']
