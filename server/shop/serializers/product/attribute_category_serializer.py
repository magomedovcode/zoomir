from shop.models import AttributeCategory
from drf_spectacular.utils import extend_schema_serializer
from rest_framework import serializers


@extend_schema_serializer(component_name='AttributeCategory')
class AttributeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributeCategory
        fields = [
            'id',
            'name'
        ]
        read_only_fields = fields
