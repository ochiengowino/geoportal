from django.urls import path, include
from rest_framework import routers
from django.shortcuts import render, redirect

from . import views

router = routers.DefaultRouter()

router.register(r'geoportal/api/counties', views.CountiesViewset,
                basename='countiesdata')
router.register(r'geoportal/api/srtm', views.RasterViewSet,
                basename='rasterdata')

urlpatterns = [
    path('', include(router.urls)),

]

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('api/counties', views.counties_api, name='counties'),
#     path('dashboard/', views.dashboard, name='dashboard'),
#     path('login/', views.user_login, name='login'),
#     path('signup/', views.user_signup, name='signup'),
#     path('set_password/<int:user_id>/', views.set_password, name='set_password'),
#     path('logout/', views.user_logout, name='logout'),
#     # path('dashboard/', views.user_dash, name='dash'),
# ]
