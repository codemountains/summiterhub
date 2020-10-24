from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authen/', include('djoser.urls.jwt')),
    path('v1/users/', include('users.urls')),
    path('v1/news/', include('news.urls')),
    path('v1/gears/', include('gears.urls')),
    path('v1/plans/', include('plans.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
