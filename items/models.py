from django.db import models

# Create your models here.

class Item(models.Model):
    item_name = models.CharField(max_length=200)
    register_date = models.DateTimeField("Item Register Date")
    was_it_removed = models.BooleanField("Item Removed")