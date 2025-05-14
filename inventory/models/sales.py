import datetime

from django.db import models



class SalesOrder(models.Model):
    warehouse_id = models.ForeignKey('warehouse.WarehouseWithUnitOfMeasurement', on_delete=models.RESTRICT)
    price_in_pack = models.DecimalField(max_digits=1000000, decimal_places=2)
    price_in_unit = models.DecimalField(max_digits=1000000, decimal_places=2)
    price_tablets_per_blister = models.DecimalField(max_digits=1000000, decimal_places=2)
    pack_quantity = models.IntegerField()
    unit_quantity = models.IntegerField()
    tablets_per_blister = models.IntegerField()
    sum_price = models.DecimalField(max_digits=1000000, decimal_places=2)
    created_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Sales Order'
        verbose_name_plural = 'Sales Orders'
        db_table = 'sales_order'


