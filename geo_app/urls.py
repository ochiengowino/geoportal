from django.urls import path
from django.shortcuts import render, redirect

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/counties', views.counties_api, name='counties'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('set_password/<int:user_id>/', views.set_password, name='set_password'),
    path('logout/', views.user_logout, name='logout'),
    # path('dashboard/', views.user_dash, name='dash'),
]
