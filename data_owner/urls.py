from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views 

urlpatterns = [
    path('data_owner', views.data_owner, name='data_owner'),
    path('data_upload', views.data_upload, name='data_upload'),
    path('view_files', views.view_files, name='view_files'),
    path('profile', views.profile, name='profile'),
    path('logout', views.logout, name='logout')
]