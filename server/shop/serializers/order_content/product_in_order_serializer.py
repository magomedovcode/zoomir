from shop.models import ProductInOrder
from drf_spectacular.utils import extend_schema_serializer
from rest_framework import serializers
from shop.serializers.product_content.product_variant_serializer import ProductVariantSerializer


@extend_schema_serializer(component_name='ProductInOrder')
class ProductInOrderSerializer(serializers.ModelSerializer):
    product_variant = ProductVariantSerializer(
        read_only=True
    )

    class Meta:
        model = ProductInOrder
        fields = [
            'id',
            'price',
            'quantity',
            'product_variant'
        ]
        read_only_fields = fields
