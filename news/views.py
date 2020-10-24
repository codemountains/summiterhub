from django.shortcuts import render
from django.db.models import Q
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import ValidationError
from .serializers import NewsSerializer, ReadNewsSerializer
from .models import News, ReadNews


class NewsListView(generics.ListAPIView):
	"""
	ニュース ListAPIView
	"""
	serializer_class = NewsSerializer
	permission_classes = (AllowAny,)
	queryset = News.objects.all()


class ReadNewsCreateView(generics.CreateAPIView):
	"""
	既読ニュース CreateAPIView
	"""
	serializer_class = ReadNewsSerializer
	queryset = ReadNews.objects.all()

	def get_queryset(self):
		return self.queryset.filter(user_id=self.request.user)

	def perform_create(self, serializer):
		try:
			serializer.save(user_id=self.request.user)
		except BaseException:
			raise ValidationError('既読済みです')
