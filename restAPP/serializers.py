from rest_framework import serializers
from restAPP.models import Customer, Purchase


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    total_purchase = serializers.IntegerField()

    class Meta:
        model = Customer
        fields = ['name', 'date', 'vip', 'phone', 'total_purchase']


class PurchaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Purchase
        fields = ['purchase_date', 'item_number', 'mask']
