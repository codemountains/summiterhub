from rest_framework.pagination import PageNumberPagination


class GearPagination(PageNumberPagination):
	page_query_param = 'page'
	last_page_strings = ('last',)
