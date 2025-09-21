from rest_framework.pagination import PageNumberPagination


class ProductPagination(PageNumberPagination):
    """
    Пагинация для списка продуктов:
    - По умолчанию 40 элементов на страницу
    - Можно задать через ?page_size=
    - Максимум 100 элементов
    """
    page_size = 40
    page_size_query_param = 'page_size'
    max_page_size = 100
