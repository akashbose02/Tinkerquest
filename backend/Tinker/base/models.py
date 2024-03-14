from django.db import models

class SKU(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    threshold = models.IntegerField(default=0)  # Threshold for inventory alerts

    def __str__(self):
        return self.name

class InventoryItem(models.Model):
    sku = models.ForeignKey(SKU, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    location = models.CharField(max_length=100)
    expiry_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.sku.name} - {self.location}"

class StockMovement(models.Model):
    item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    quantity_changed = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.item.sku.name} - {self.timestamp}"

class SalesOrder(models.Model):
    items = models.ManyToManyField(InventoryItem)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Sales Order {self.id}"
