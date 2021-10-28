from django.contrib import admin
from django.urls import path
from . import views
# from django.urls.conf import include

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.handlesignup,name="handlesignup"),
    path('login/', views.handlelogin,name="handlelogin"),
    path('logout/', views.handlelogout,name="handlelogout"),
    path('categories/', views.categories, name='categories'),
    path('subcategories/', views.subcategories, name='subcategories'),
    path('jobs/', views.jobs, name='jobs'),
    path('company_details/', views.company_details, name='company_details'),
    path('searchstate', views.searchstate, name='searchstate'),
    path('searchcat', views.searchcat, name='searchcat'),
    path('searchsubcat', views.searchsubcat, name='searchsubcat'),
    path('searchjob', views.searchjob, name='searchjob'),
     
]
