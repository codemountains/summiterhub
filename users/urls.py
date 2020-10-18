from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('detail', views.UserDetailViewSet)

urlpatterns = [
	path('create/', views.CreateUserView.as_view(), name='create'),
	path('update/', views.UpdateUserView.as_view(), name='update'),
	path('delete/', views.DeleteUserView.as_view(), name='delete'),
	path('', include(router.urls)),
]
