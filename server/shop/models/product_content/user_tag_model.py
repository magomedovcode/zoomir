from django.db import models
from django.conf import settings
from shop.models.product_content.tag_model import Tag


class UserTag(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="tag_preferences",
        verbose_name="Пользователь"
    )
    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,
        related_name="user_preferences",
        verbose_name="Тег"
    )
    weight = models.PositiveIntegerField(
        default=1,
        verbose_name="Вес интереса"
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'tag'],
                name='unique_tag_per_user'
            )
        ]
        verbose_name = "Интерес пользователя (тег)"
        verbose_name_plural = "Интересы пользователей"

    def __str__(self):
        return f"{self.user.username} → {self.tag.name} ({self.weight})"
