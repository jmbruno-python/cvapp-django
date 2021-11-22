from django.urls import path
from . import views

urlpatterns = [
    # Double single quotes render the homepage
    path('', views.home, name="home"),
]
