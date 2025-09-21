from drf_spectacular.utils import extend_schema
from shop.models import Country
from shop.serializers import CountrySerializer
from rest_framework import (
    generics,
    permissions
)


@extend_schema(tags=['Страны производства'])
class CountryListView(generics.ListAPIView):
    """
    Получение списка всех стран производителей
    """
    serializer_class = CountrySerializer
    permission_classes = [permissions.AllowAny]
    queryset = Country.objects.all()
