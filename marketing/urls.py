from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views
from . import views


app_name='marketing'
urlpatterns=[
    path('', views.index, name='index'),
    path('product/', views.product, name='product'),

]