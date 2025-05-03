import datetime

from django.db import models

from warehouse.models.WarehouseWithUnitOfMeasurement import Warehouse


class Receipt(models.Model):
    entry_date = models.DateField(default=datetime.date.today)
    warehouse_id = models.ForeignKey(Warehouse, on_delete=models.RESTRICT)
    box_quantity = models.IntegerField()
    purchase_price = models.DecimalField(max_digits=1000000, decimal_places=2)
    sale_price = models.DecimalField(max_digits=1000000, decimal_places=2)



