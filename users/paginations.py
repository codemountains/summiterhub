from rest_framework.pagination import PageNumberPagination


class FriendPagination(PageNumberPagination):
	page_query_param = 'page'
	last_page_strings = ('last',)


class PartyPagination(PageNumberPagination):
	page_query_param = 'page'
	last_page_strings = ('last',)
