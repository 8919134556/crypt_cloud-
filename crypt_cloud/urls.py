"""crypt_cloud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('cloud/', include('cloud.urls')),
    path('mainapp/', include('mainapp.urls')),
    path('data_user/', include('data_user.urls')),
    path('data_owner/', include('data_owner.urls')),
    path('auditor/', include('auditor.urls')),
    path('authority/', include('authority.urls')),
    path('', RedirectView.as_view(url='cloud/', permanent=True)),
    path('', RedirectView.as_view(url='data_user/', permanent=True)),
    path('', RedirectView.as_view(url='data_owner/', permanent=True)),
    path('', RedirectView.as_view(url='auditor/', permanent=True)),
    path('', RedirectView.as_view(url='authority/', permanent=True)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
