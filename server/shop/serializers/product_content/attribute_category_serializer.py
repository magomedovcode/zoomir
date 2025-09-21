from shop.models import AttributeCategory
from drf_spectacular.utils import extend_schema_serializer
from rest_framework import serializers
from shop.serializers.product_content.attribute_serializer import AttributeSerializer


@extend_schema_serializer(component_name='AttributeCategory')
class AttributeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributeCategory
        fields = [
            'id',
            'name'
        ]
        read_only_fields = fields


@extend_schema_serializer(component_name='AttributesPerCategory')
class AttributesPerCategorySerializer(serializers.ModelSerializer):
    attributes = AttributeSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = AttributeCategory
        fields = [
            'id',
            'name',
            'attributes'
        ]
        read_only_fields = fields
