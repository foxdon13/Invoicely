from django.shortcuts import render
from .models import Invoice,Item
from .serializers import InvoiceSerializer,ItemSerializer

from rest_framework import serializers, viewsets
from django.core.exceptions import PermissionDenied


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

    def get_queryset(self):
        return self.queryset.filter(created_by=self.request.user)

    def perform_create(self,serializer):
        team = self.request.teams.first()
        serializer.save(created_by=self.request.user,team=team)

    def perform_update(self,serializer):
        obj = self.get_object()

        if self.request.user != obj.created_by:
            raise PermissionDenied("Wrong Object owner")
         
        serializer.save()


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get_queryset(self):
        invoice_id = self.request.GET.get('invoice_id',0)
        return self.queryset.filter(invoice__id=invoice_id)