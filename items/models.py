from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=200)
    number_cellphone = models.CharField(max_length=20)
    relationship = models.CharField(max_length=30)
    cpf_person = models.CharField(max_length=30)
class Item(models.Model):
    item_name = models.CharField(max_length=100)
    register_date = models.DateTimeField("Item Register Date")
    withdraw_date = models.DateTimeField("Item Withdraw Date", null=True, blank=True)
    was_it_removed = models.BooleanField("Item Removed")
    found_item_person = models.ForeignKey(Person, on_delete=models.PROTECT, related_name="items_found")
    owner_item = models.ForeignKey(Person, on_delete=models.PROTECT, related_name="items_owned", null=True, blank=True)