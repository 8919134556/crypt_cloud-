from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views 

urlpatterns = [
    path('authority_home', views.authority_home, name='authority_home'),
    path('accept/<int:id>', views.accept, name='accept'),
    path('reject/<int:id>', views.reject, name='reject'),
    path('authority_logout', views.authority_logout, name='authority_logout'),
]