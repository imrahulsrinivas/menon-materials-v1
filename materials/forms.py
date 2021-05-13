from django import forms

from .models import MaterialRequest, SupplierQuotation

class DateInput(forms.DateInput):
    input_type = "date"

    def __init__(self, **kwargs):
        kwargs["format"] = "%Y-%m-%d"
        super().__init__(**kwargs)

class MaterialRequestForm(forms.ModelForm):
	class Meta:
		model = MaterialRequest
		exclude = ['created_at','updated_at','sent_to_all_suppliers','created_by','quote_selected']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields["date_required_by"].widget = DateInput()

class SupplierQuotationForm(forms.ModelForm):
	class Meta:
		model = SupplierQuotation
		exclude = ['created_at','updated_at','created_by','material_request','quote_status']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields["date_of_supply"].widget = DateInput()