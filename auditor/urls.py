from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views 

urlpatterns = [
    path('auditor_home', views.auditor_home, name='auditor_home'),
    path('revoke', views.revoke, name='revoke'),
    path('trace', views.trace, name='trace'),
    path('details', views.details, name='details'),
    path('auditor_logout', views.auditor_logout, name='auditor_logout'),
    path('auditor_revoke/<email>/<int:id>', views.auditor_revoke, name='auditor_revoke'),
    path('auditor_accept/<email>/<int:id>', views.auditor_accept, name='auditor_accept'),

]