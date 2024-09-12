# django_hairstore/urls.py

from django.contrib import admin
from django.urls import include, path
from appointments.views import signup

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('appointments.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # Includes login/logout views
    path('signup/', signup, name='signup'),  # Custom sign-up view
]