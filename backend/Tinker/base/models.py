from django.db import models
from django.contrib.auth.models import User

class InventoryItem(models.Model):
    name = models.CharField(max_length=200, default="")
    quantity = models.IntegerField(default=0)
    description = models.TextField(default="")
    date_created = models.DateTimeField(auto_now_add=True)
    threshold = models.IntegerField(default=0)
    location = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.name
