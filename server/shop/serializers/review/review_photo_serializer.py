from shop.models import ReviewPhoto
from drf_spectacular.utils import extend_schema_serializer
from rest_framework import serializers


@extend_schema_serializer(component_name='ReviewPhoto')
class ReviewPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewPhoto
        fields = [
            'id',
            'photo'
        ]
        read_only_fields = fields
