from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class EmployeeInline(admin.StackedInline):
    model = Employee
    verbose_name_plural = 'employee'


class UserAdmin(BaseUserAdmin):
    inlines = (EmployeeInline,)

# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
# admin.site.register(Customer)
# admin.site.register(Employee)