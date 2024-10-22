# appointments/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_homepage, name='homepage'),  
    path('book/', views.book_appointment, name='book_appointment'),
    path('faq/', views.faq_view, name='faq'), 
]
