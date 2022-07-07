from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views 

urlpatterns = [
    path('data_user', views.data_user, name='data_user'),
    path('search_files', views.search_files, name='search_files'),
    path('file_request/<int:id>/<email>', views.file_request, name='file_request'),
    path('my_download', views.my_download, name='my_download'),
    path('download', views.download, name='download'),
    path('my_pro', views.my_pro, name='my_pro'),
    path('user_logout', views.user_logout, name='user_logout'),
]