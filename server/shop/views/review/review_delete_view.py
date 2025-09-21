from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from shop.models import Review
from shop.serializers import ReviewSerializer
from rest_framework import (
    generics,
    permissions,
    status
)


@extend_schema(tags=['Отзывы'])
class ReviewDeleteView(generics.DestroyAPIView):
    """
    Удаление отзыва
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
