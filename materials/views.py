from django.shortcuts import render

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse
import json

# DRF RELATED
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, BasePermission, BasePermission
from rest_framework import status
from rest_framework.response import Response

from django.views.decorators.csrf import csrf_protect


from django.contrib.auth.decorators import login_required, permission_required
from django.urls import reverse_lazy

from django.utils.translation import ugettext as _
import django


from django.contrib.auth.decorators import login_required, permission_required
import logging
logger = logging.getLogger()
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, get_object_or_404, redirect

import materials.serializers as materials_serializers
import materials.forms as materials_forms

from website.pretty_printing import dumps
from sorcery import dict_of

from .models import MaterialRequest, SupplierQuotation
from .forms import MaterialRequestForm, SupplierQuotationForm
from django.contrib import messages
from django.db.models import OuterRef, Subquery, Prefetch


# Create your views here.
@login_required(login_url=reverse_lazy('login'))
def index(request):
     try:
          supplier = request.user.core_supplier_user
          type_user = "supplier"
          return redirect(reverse('materials:suppliers'))
     except Exception as e:
          logger.exception("user error")

          
     try:
          employee = request.user.core_employee_user
          type_user = "employee"
          return redirect(reverse('materials:employees_material_requests_simple'))
     except Exception as e:
          logger.exception("user error")

     return redirect(reverse('login'))

# Create your views here.
@login_required(login_url=reverse_lazy('login'))
def employees_material_requests_simple(request):

     mat_reqs = MaterialRequest.objects.select_related('quote_selected').prefetch_related(Prefetch('materials_supplierquotation_material_request',queryset = SupplierQuotation.objects.all().select_related('created_by')))
     return render(request, 'materials/employees_material_requests_simple.html',dict(mat_reqs=mat_reqs,title="List of Material Requests"))



@login_required(login_url=reverse_lazy('login'))
def employees_material_requests_simple_add(request):
     if request.method == 'POST':
          form = MaterialRequestForm(request.POST)
          if form.is_valid():
               obj2 = form.save(commit=False)
               obj2.created_by = request.user
               obj2.save()
               messages.success(request, 'Record Added')
               return redirect(reverse('materials:employees_material_requests_simple'))
          else:
               messages.success(request, 'Record Not Added')
               return render(request, 'materials/employees_material_requests_simple_add.html',dict(form=form,title="Add new material request"))
     else:
          form = MaterialRequestForm()
          return render(request, 'materials/employees_material_requests_simple_add.html',dict(form=form,title="Add new material request"))


@login_required(login_url=reverse_lazy('login'))
def employees_material_requests_simple_delete(request, id):
     try:
          query = MaterialRequest.objects.get(id=id)
          query.delete()
          messages.success(request, 'Record Deleted')
          return redirect(reverse('materials:employees_material_requests_simple'))
     except Exception as e:
          messages.error(request, 'Unable to Delete')
          return redirect(reverse('materials:employees_material_requests_simple'))


@login_required(login_url=reverse_lazy('login'))
def employees_material_requests_simple_sent_to_all_suppliers(request,id):
     if request.method == 'POST':
          try:
               query = MaterialRequest.objects.get(id=id)
               query.sent_to_all_suppliers = True
               query.save()
               messages.success(request, 'Sent to all Suppliers')
               return redirect(reverse('materials:employees_material_requests_simple'))
          except Exception as e:
               messages.error(request, 'Unable to Send')
               return redirect(reverse('materials:employees_material_requests_simple'))
     else:
          return redirect(reverse('materials:employees_material_requests_simple'))


@login_required(login_url=reverse_lazy('login'))
def suppliers(request):
     mat_reqs = MaterialRequest.objects.prefetch_related('materials_supplierquotation_material_request').filter(sent_to_all_suppliers=True)
     return render(request, 'materials/suppliers_main.html',dict(mat_reqs=mat_reqs,title="List of Material Requests"))


@login_required(login_url=reverse_lazy('login'))
def suppliers_apply(request,id):
     obj = MaterialRequest.objects.get(id=id)
     if request.method == 'POST':
          form = SupplierQuotationForm(request.POST)
          if form.is_valid():
               obj2 = form.save(commit=False)
               obj2.created_by = request.user
               obj2.material_request = obj
               obj2.save()
               messages.success(request, 'Applied')
               return redirect(reverse('materials:suppliers'))
          else:
               return render(request, 'materials/suppliers_apply.html',dict(form=form,title="Apply material request",obj=obj))
     else:
          form = SupplierQuotationForm()
          return render(request, 'materials/suppliers_apply.html',dict(form=form,title="Apply material request",obj=obj))


@login_required(login_url=reverse_lazy('login'))
def employees_material_requests_simple_select_supplier(request,id,quotation_id=None):
     obj = MaterialRequest.objects.get(id=id)
     if request.method == 'POST':
          try:
               quote_selected = obj.materials_supplierquotation_material_request.get(id=quotation_id)
               quote_selected.quote_status = "approved"
               quote_selected.save()
               obj.quote_selected = quote_selected
               obj.save()
               messages.success(request, 'Supplier Selected')
               return redirect(reverse('materials:employees_material_requests_simple'))
          except Exception as e:
               messages.error(request, 'Unable to Send')
               return redirect(reverse('materials:employees_material_requests_simple'))
     else:
          quotes = obj.materials_supplierquotation_material_request.all().select_related('created_by')
          return render(request, 'materials/employees_material_requests_simple_select_supplier.html',dict(quotes=quotes,title="Select material Suppliers",obj=obj))


@login_required(login_url=reverse_lazy('login'))
def goods_delivered(request,id):
     obj = SupplierQuotation.objects.get(id=id)
     if request.method == 'POST':
          try:
               obj.quote_status = "goods_dispatched"
               obj.save()
               messages.success(request, 'Status changed to Goods Dispatched')
               return redirect(reverse('materials:suppliers'))
          except Exception as e:
               messages.error(request, 'Unable to Send')
               return redirect(reverse('materials:suppliers'))
     else:
          messages.success(request, 'NOt a post request')
          return redirect(reverse('materials:suppliers'))