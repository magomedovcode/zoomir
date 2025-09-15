from shop.models import ProductCategory
from drf_spectacular.utils import extend_schema_serializer
from rest_framework import serializers
from shop.serializers import ProductChapterSerializer


@extend_schema_serializer(component_name='ProductCategory')
class ProductCategorySerializer(serializers.ModelSerializer):
    product_chapter = ProductChapterSerializer(
        read_only=True
    )
    class Meta:
        model = ProductCategory
        fields = [
            'id',
            'name',
            'product_chapter'
        ]
        read_only_fields = fields
