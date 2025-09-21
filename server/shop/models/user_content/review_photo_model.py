import os
import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from shop.models.user_content.review_model import Review


def review_photo_path(instance, filename):
    ext = os.path.splitext(filename)[1]
    return f'photos/reviews/{uuid.uuid4()}{ext}'


class ReviewPhoto(models.Model):
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        verbose_name=_('Отзыв к товару'),
        help_text=_('Выберите отзыв к товару'),
        related_name='review_photos'
    )
    photo = models.ImageField(
        verbose_name=_('Фотография к отзыву'),
        upload_to=review_photo_path,
        help_text=_('Загрузите фотографию к отзыву')
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['review', 'photo'],
                name='unique_photo_per_review'
            )
        ]
        verbose_name = _('Фотография для отзыва')
        verbose_name_plural = _('Фотографии для отзыва')
        ordering = ['-id']

    def __str__(self):
        return f'Фотография для {self.review.title}'
