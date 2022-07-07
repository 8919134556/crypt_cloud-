from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views 

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    
    path('cloud', views.cloud, name='cloud'),
    path('contact', views.contact, name='contact'),
    path('authority', views.authority, name='authority'),
    path('auditor', views.auditor, name='auditor'),
    path('data_owner_reg', views.data_owner_reg, name='data_owner_reg'),
    path('data_user_reg', views.data_user_reg, name='data_user_reg'),
    path('data_owner_login', views.data_owner_login, name='data_owner_login'),
    path('data_user_login', views.data_user_login, name='data_user_login'),
]