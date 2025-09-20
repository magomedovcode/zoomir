from shop.models import Attribute
from drf_spectacular.utils import extend_schema_serializer
from rest_framework import serializers
from shop.serializers.product_content.attribute_category_serializer import AttributeCategorySerializer


@extend_schema_serializer(component_name='Attribute')
class AttributeSerializer(serializers.ModelSerializer):
    attribute_category = AttributeCategorySerializer(
        read_only=True
    )

    class Meta:
        model = Attribute
        fields = [
            'id',
            'name',
            'value',
            'attribute_category'
        ]
        read_only_fields = fields
