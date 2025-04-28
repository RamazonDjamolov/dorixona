from  django import forms

from warehouse.models.WarehouseWithUnitOfMeasurement import ProductWithUnit


class ProductWithUnitForm(forms.ModelForm):
    class Meta:
        model = ProductWithUnit
        fields = "__all__"


