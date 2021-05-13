from django.db import models
from django.contrib.auth.models import User



class Employee(models.Model):

    DEPARTMENT = (
        ("materials", "MATERIALS"),
        ("marketing", 'MARKETING'),
    )

    user = models.OneToOneField(User, related_name="%(app_label)s_%(class)s_user", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    department = models.CharField(max_length=100,choices=DEPARTMENT,default="materials")

    def __str__(self):
        return str(self.name)

class Customer(models.Model):
    user = models.OneToOneField(User, related_name="%(app_label)s_%(class)s_user", on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=12, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.name)


class Supplier(models.Model):
    user = models.OneToOneField(User, related_name="%(app_label)s_%(class)s_user", on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=12, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.name)
    