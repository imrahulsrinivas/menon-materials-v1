from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class MaterialRequest(models.Model):
	material_name = models.CharField(max_length = 50)
	quantity = models.FloatField()
	date_required_by = models.DateTimeField()
	sent_to_all_suppliers = models.BooleanField(default=False)
	quote_selected = models.ForeignKey('materials.SupplierQuotation',related_name="%(app_label)s_%(class)s_quote_selected",null=True,on_delete=models.SET_NULL)
	created_by = models.ForeignKey(User,related_name="%(app_label)s_%(class)s_created_by",on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


QUOTE_STATUS = (
	("pending", "PENDING"),
    ("approved", "APPROVED"),
    ("goods_dispatched", 'GOODS_DISPATCHED'),
    ("goods_recieved", 'GOODS_RECIEVED'),
)

# Create your models here.
class SupplierQuotation(models.Model):
	material_request = models.ForeignKey(MaterialRequest,related_name="%(app_label)s_%(class)s_material_request",on_delete=models.CASCADE)
	quantity = models.FloatField()
	date_of_supply = models.DateTimeField()
	created_by = models.ForeignKey(User,related_name="%(app_label)s_%(class)s_created_by",on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	quote_status = models.CharField(max_length=100,choices=QUOTE_STATUS,default="pending")

	class Meta:
		unique_together = ('material_request','created_by')
