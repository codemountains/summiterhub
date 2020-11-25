from rest_framework.pagination import PageNumberPagination


class NewsPagination(PageNumberPagination):
	page_query_param = 'page'
	last_page_strings = ('last',)
