from django.contrib import admin
from nested_admin.nested import NestedModelAdmin
from shop.models import ReviewPhoto


@admin.register(ReviewPhoto)
class ReviewPhotoAdmin(NestedModelAdmin):
    list_display = ('review', 'photo')
    list_filter = ('review', )
    ordering = ['-id']
    autocomplete_fields = ['review']
    list_per_page = 20

    fieldsets = (
        ('Выберите параметры', {
            'fields': ('review', )
        }),
        ('Заполните поля', {
            'fields': ('photo', ),
        }),
    )
