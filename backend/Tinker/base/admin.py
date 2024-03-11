from django.contrib import admin
from .models import SKU, InventoryItem, SalesOrder, StockMovement

admin.site.register(SKU)
admin.site.register(InventoryItem)
admin.site.register(SalesOrder)
admin.site.register(StockMovement)