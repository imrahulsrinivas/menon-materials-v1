"""website URL Configuration

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
from django.conf.urls import url
from django.urls import path, include, re_path
from django.contrib.auth.views import LoginView, LogoutView
from marketing.forms import LoginForm
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from django.conf.urls import  url
from django.views.static import serve
from django.conf import settings


urlpatterns = [
    path('', include('core.urls')),
    path('', include('pages.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(form_class=LoginForm)),
    path('accounts/logout/', login_required(auth_views.LogoutView.as_view())),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('marketing/', include('marketing.urls')),
    path('materials/',include('materials.urls')),
    
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]


