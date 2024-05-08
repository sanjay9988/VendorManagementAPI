
from django.utils import timezone
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from .models import  PurchaseOrder
from .serializers import PurchaseOrderSerializer

from django_filters.rest_framework import DjangoFilterBackend
from .filters import PurchaseOrderFilter

class PurchaseOrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PurchaseOrderFilter




class PurchaseOrderRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer


class AcknowledgePurchaseOrderAPIView(generics.UpdateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.acknowledgment_date = timezone.now()
        instance.save()
        return Response({'message': 'Purchase order acknowledged successfully.'})


