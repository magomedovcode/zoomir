from drf_spectacular.utils import extend_schema_serializer
from rest_framework import serializers
from shop.models import Review


@extend_schema_serializer(component_name='Review')
class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Review
        fields = [
            'id',
            'user',
            'title',
            'comment',
            'rating',
            'date'
        ]
        read_only_fields = fields


@extend_schema_serializer(component_name='ReviewCreate')
class ReviewCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Review
        fields = [
            'user',
            'title',
            'rating',
            'comment'
        ]
