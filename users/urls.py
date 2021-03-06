from django.urls import path, include
from rest_framework import routers
from . import views

# Users me
router = routers.DefaultRouter()
router.register('details', views.UserDetailViewSet)
router.register('', views.UserViewSet)

# Friends
friend_router = routers.DefaultRouter()
friend_router.register('requests', views.FriendRequestViewSet)
friend_router.register('blocking', views.BlockingFriendViewSet)
friend_router.register('', views.FriendViewSet)

# Friends detail
friend_detail_router = routers.DefaultRouter()
friend_detail_router.register('', views.FriendDetailViewSet)

# Blocking friend detail
blocking_detail_router = routers.DefaultRouter()
blocking_detail_router.register('', views.BlockingFriendDetailViewSet)

# Parties
party_router = routers.DefaultRouter()
party_router.register('', views.PartyViewSet)

# Party members
party_member_router = routers.DefaultRouter()
party_member_router.register('', views.PartyMemberViewSet)

# Party member details
party_member_detail_router = routers.DefaultRouter()
party_member_detail_router.register('', views.PartyMemberDetailViewSet)

urlpatterns = [
	path('signup/', views.CreateUserView.as_view(), name='signup'),
	path(
		'tokens/create/',
		views.UserTokenCreateView.as_view(),
		name='tokens_create'
	),
	path(
		'tokens/activate/<uuid:pk>/',
		views.UserTokenUpdateView.as_view(),
		name='tokens_activate'
	),
	path('friends/', include(friend_router.urls)),
	path(
		'friends/<uuid:friend_id>/details/',
		include(friend_detail_router.urls)
	),
	path(
		'friends/blocking/<uuid:blocking_friend_id>/details/',
		include(blocking_detail_router.urls)
	),
	path('parties/', include(party_router.urls)),
	path(
		'parties/<uuid:party_id>/members/',
		include(party_member_router.urls)
	),
	path(
		'parties/<uuid:party_id>/members/<uuid:party_member_id>/details/',
		include(party_member_detail_router.urls)
	),
	path('me/', include(router.urls)),
]
