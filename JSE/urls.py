from django.contrib import admin
from django.urls import path
from . import views
# from django.urls.conf import include

urlpatterns = [
    path('', views.home, name='home')
     
]
