from shop.models import ProductChapter
from drf_spectacular.utils import extend_schema_serializer
from rest_framework import serializers

@extend_schema_serializer(component_name='ProductChapter')
class ProductChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductChapter
        fields = [
            'id',
            'name'
        ]
        read_only_fields = fields
