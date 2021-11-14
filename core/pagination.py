from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

class MyPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'p'
    page_size_query_param = 'records'
    max_page_size = 7
    last_page_strings = 'end'


class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 5
    limit_query_param = 'm'
    offset_query_param = 'o'
    max_limit = 2