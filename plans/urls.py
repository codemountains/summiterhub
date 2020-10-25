from django.urls import path, include
from rest_framework import routers
from . import views

# Plans & Bookmarks
plan_router = routers.DefaultRouter()
plan_router.register('bookmarks', views.BookmarkViewSet)
plan_router.register('search', views.PlanSearchViewSet)
plan_router.register('', views.PlanViewSet)


# Plan details (gear, custom gear, routes, escape routes)
plan_details_router = routers.DefaultRouter()
plan_details_router.register('gears', views.PlanGearViewSet)
plan_details_router.register('customgears', views.PlanCustomGearViewSet)
plan_details_router.register('routes', views.PlanRouteViewSet)
plan_details_router.register('escaperoutes', views.PlanEscapeRouteViewSet)
plan_details_router.register('members', views.PlanMemberViewSet)


# Plan route details
plan_route_router = routers.DefaultRouter()
plan_route_router.register('details', views.PlanRouteDetailViewSet)


urlpatterns = [
	path('', include(plan_router.urls)),
	path('<uuid:plan_id>/', include(plan_details_router.urls)),
	path(
		'<uuid:plan_id>/routes/<uuid:plan_route_id>/',
		include(plan_route_router.urls)
	),
]
