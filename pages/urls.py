from . import views
from django.urls import path

app_name='pages'
urlpatterns=[
    path('', views.home, name='home'),
]