from drf_spectacular.utils import extend_schema_serializer
from rest_framework import serializers
from django.contrib.auth.models import User


@extend_schema_serializer(component_name='User')
class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]
