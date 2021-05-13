from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views
from . import views


app_name='materials'
urlpatterns=[
    path('', views.index, name='index'),

    path('employees_material_requests_simple/', views.employees_material_requests_simple , name='employees_material_requests_simple'),
    path('employees_material_requests_simple/add', views.employees_material_requests_simple_add , name='employees_material_requests_simple_add'),
    path('employees_material_requests_simple/delete/<int:id>/', views.employees_material_requests_simple_delete, name='employees_material_requests_simple_delete'),
    path('employees_material_requests_simple/sent_to_all_suppliers/<int:id>/', views.employees_material_requests_simple_sent_to_all_suppliers, name='employees_material_requests_simple_sent_to_all_suppliers'),
    path('employees_material_requests_simple/select_supplier/<int:id>/<int:quotation_id>/', views.employees_material_requests_simple_select_supplier, name='employees_material_requests_simple_select_supplier'),



    path('suppliers',views.suppliers,name='suppliers'),
    path('suppliers/apply/<int:id>',views.suppliers_apply,name='suppliers_apply'),
    path('suppliers/goods_delivered/<int:id>',views.goods_delivered,name='goods_delivered')


]