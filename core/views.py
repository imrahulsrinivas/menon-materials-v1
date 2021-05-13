from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
from django.contrib.auth.decorators import login_required, permission_required
import logging
logger = logging.getLogger()
import snoop

# REFACTOR CODE
@snoop
def welcome(request):
    if request.user.is_authenticated:
        user = User.objects.get(username = request.user.username)

        try:
            supplier = user.core_supplier_user
            type_user = "supplier"
            return redirect(reverse('materials:index'))
        except Exception as e:
            logger.exception("user error")

        try:
            department = user.core_employee_user.department

            if department == "marketing":
                return redirect(reverse('marketing:index'))
            elif department == "materials":
                return redirect(reverse('materials:employees_material_requests_simple'))
        except:
            logger.exception("user error")


    else:
        return redirect(reverse('login'))