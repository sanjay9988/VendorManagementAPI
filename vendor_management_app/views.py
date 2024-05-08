from rest_framework import generics,viewsets,status
from rest_framework.response import Response
from django.db.models import Count, Avg,Sum
from .models import Vendor,HistoricalPerformance
from .serializers import VendorSerializer, HistoricalPerformanceSerializer,VendorStatisticsSerializer
from purchase_order_app import models
from django.utils import timezone

from rest_framework.views import APIView

from purchase_order_app.models import PurchaseOrder


class VendorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorPerformanceAPIView(APIView):

    def get(self, request, pk=None):
        vendor = self.get_vendor(pk)
        if not vendor:
            return Response({"error": "Vendor not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer=VendorStatisticsSerializer(vendor)
        return Response(serializer.data)

    def get_vendor(self, pk):
        try:
            return Vendor.objects.get(id=pk)
        except Vendor.DoesNotExist:
            return None




        
class HistoricalPerformanceListCreateAPIView(generics.ListCreateAPIView):
    queryset = HistoricalPerformance.objects.all()
    serializer_class = HistoricalPerformanceSerializer

class HistoricalPerformanceRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HistoricalPerformance.objects.all()
    serializer_class = HistoricalPerformanceSerializer
