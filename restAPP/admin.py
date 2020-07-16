from django.contrib import admin
from .models import Customer, Purchase
from django.utils.html import format_html
from phone_field import PhoneField
# Register your models here.




# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'date', 'vip', 'phone']


admin.site.register(Customer, CustomerAdmin)


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ["customer", "purchase_date", "item_number", "mask"]


admin.site.register(Purchase, PurchaseAdmin)