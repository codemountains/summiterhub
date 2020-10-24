from django.urls import path
from . import views


urlpatterns = [
	path('read/', views.ReadNewsCreateView.as_view(), name='read'),
	path('', views.NewsListView.as_view(), name='news'),
]
