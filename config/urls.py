from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/partner', include('partner.urls')),
    path('api/sponsor', include('sponsor.urls')),
    path('api/event', include('event.urls')),
]
