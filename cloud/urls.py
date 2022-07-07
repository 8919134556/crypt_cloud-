from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views 

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('d_owner', views.d_owner, name='d_owner'),
    path('d_user', views.d_user, name='d_user'),
    path('data_access', views.data_access, name='data_access'),
    path('cloud_logout', views.cloud_logout, name='cloud_logout'),
    path('owner_accept/<int:id>', views.owner_accept, name='owner_accept'),
    path('owner_reject/<int:id>', views.owner_reject, name='owner_reject'),
    path('user_accept/<int:id>', views.user_accept, name='user_accept'),
    path('user_reject/<int:id>', views.user_reject, name='user_reject'),
    path('data_accept/<int:id>', views.data_accept, name='data_accept'),
    path('data_reject/<int:id>', views.data_reject, name='data_reject'),
]