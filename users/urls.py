from django.urls import path, include
from rest_framework import routers
from . import views


# User
router = routers.DefaultRouter()
router.register('detail', views.UserDetailViewSet)
router.register('', views.UserViewSet)


# Friend
friend_router = routers.DefaultRouter()
friend_router.register('request', views.FriendRequestViewSet)
friend_router.register('blocking', views.BlockingFriendViewSet)
friend_router.register('', views.FriendViewSet)


# Party
party_router = routers.DefaultRouter()
party_router.register('/member', views.PartyMemberViewSet)
party_router.register('', views.PartyViewSet)


urlpatterns = [
	path('signup/', views.CreateUserView.as_view(), name='signup'),
	path('friend/', include(friend_router.urls)),
	path('party/', include(party_router.urls)),
	path('', include(router.urls)),
]
