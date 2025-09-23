from django.contrib.auth.models import User
from drf_spectacular.types import OpenApiTypes
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from drf_spectacular.utils import (
    extend_schema_field,
    extend_schema_serializer
)


@extend_schema_serializer(component_name='User')
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    access = serializers.SerializerMethodField()
    refresh = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["id", "username", "password", "access", "refresh"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
        )
        return user

    @extend_schema_field(OpenApiTypes.ANY)
    def get_access(self, obj):
        refresh = RefreshToken.for_user(obj)
        return str(refresh.access_token)

    @extend_schema_field(OpenApiTypes.ANY)
    def get_refresh(self, obj):
        refresh = RefreshToken.for_user(obj)
        return str(refresh)
