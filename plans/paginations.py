from rest_framework.pagination import PageNumberPagination


class PlanBasePagination(PageNumberPagination):
	page_query_param = 'page'
	last_page_strings = ('last',)
