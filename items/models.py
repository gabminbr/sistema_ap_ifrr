import datetime

from django.db import models
from django.utils import timezone
# Create your models here.

class Person(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    number_cellphone = models.CharField(max_length=20)
    relationship = models.CharField(max_length=30)
    cpf_person = models.CharField(max_length=30)
class Item(models.Model):

    def __str__(self):
        return self.item_name
    
    def was_registered_recently(self):
        return self.register_date >= timezone.now() - datetime.timedelta(days=1)

    STATUS_CHOICE = [
        ('lost', 'LOST'),
        ('found', 'FOUND'),
        ('returned', 'RETURNED'),
    ]

    item_name = models.CharField(max_length=100)
    register_date = models.DateTimeField("Item Register Date")
    withdraw_date = models.DateTimeField("Item Withdraw Date", null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='lost')
    found_item_person = models.ForeignKey(Person, on_delete=models.PROTECT, related_name="items_found")
    owner_item = models.ForeignKey(Person, on_delete=models.PROTECT, related_name="items_owned", null=True, blank=True)