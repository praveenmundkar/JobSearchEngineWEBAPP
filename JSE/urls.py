from django.contrib import admin
from django.urls import path
from . import views
# from django.urls.conf import include

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.handlesignup,name="handlesignup"),
    path('login/', views.handlelogin,name="handlelogin"),
    path('logout/', views.handlelogout,name="handlelogout")
     
]
