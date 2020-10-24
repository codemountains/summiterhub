from django.urls import path, include
from rest_framework import routers
from . import views

# Gears
gear_router = routers.DefaultRouter()
gear_router.register('', views.GearViewSet)


# Custom gears
custom_gear_router = routers.DefaultRouter()
custom_gear_router.register('', views.CustomGearViewSet)


urlpatterns = [
	path('', include(gear_router.urls)),
	path('<uuid:gear_id>/customgears/', include(custom_gear_router.urls)),
]
