from shop.models import Attribute
from drf_spectacular.utils import extend_schema_serializer
from rest_framework import serializers


@extend_schema_serializer(component_name='Attribute')
class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = [
            'id',
            'name',
            'value'
        ]
        read_only_fields = fields
