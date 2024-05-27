from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page),
    path('register', views.register_page),
    path('main', views.main)
]
