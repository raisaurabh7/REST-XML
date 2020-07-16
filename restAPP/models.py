from django.db import models
from datetime import datetime
from phone_field import PhoneField

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateField(default=datetime.now)
    vip = models.BooleanField(default=False,)
    phone = PhoneField(blank=True, help_text='Contact phone number')


class Purchase(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='CustomerPurchase')
    purchase_date = models.DateField(default=None)
    item_number = models.IntegerField()
    mask = models.BooleanField(default=False,)

