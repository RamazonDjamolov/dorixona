from django.shortcuts import redirect, render
from django.views import View

from warehouse.forms.ProductWithUnit import ProductWithUnitForm


class ProductWithUnitCreateView(View):


    def get(self, request):
        form = ProductWithUnitForm()
        return render(request, template_name='base/test.html', context={"form": form})

    def post(self, request):
        form = ProductWithUnitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("product_list")  # Redirect to product list view
        return render(request, template_name='base/test.html', context={"form": form})