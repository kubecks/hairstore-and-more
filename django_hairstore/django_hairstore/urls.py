# django_hairstore/urls.py

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('appointments.urls')),  # Includes all URLs from the appointments app
    path('accounts/', include('django.contrib.auth.urls')),  # For login and logout
]
