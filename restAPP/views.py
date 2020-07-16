from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CustomerSerializer, PurchaseSerializer
from .models import Customer, Purchase
from rest_framework import generics
from django.db.models import Count

# Create your views here.


class CustomerViewSet(generics.ListAPIView):
    serializer_class = CustomerSerializer

    def get_queryset(self):
        return Customer.objects.all().annotate(total_purchase=Count('customer_id', distinct=True))


class PurchaseList(generics.ListAPIView):
    serializer_class = PurchaseSerializer
    model = Purchase

    def get_queryset(self):
        return Purchase.objects.all()
