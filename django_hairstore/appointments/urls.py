# appointments/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_homepage, name='homepage'),  # URL for the homepage view
    path('book/', views.book_appointment, name='book_appointment'),  # URL for booking appointments
]
