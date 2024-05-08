from django.urls import path

from .views import (
    VendorListCreateAPIView,
    VendorRetrieveUpdateDestroyAPIView,
    VendorPerformanceAPIView,
    HistoricalPerformanceListCreateAPIView,
    HistoricalPerformanceRetrieveUpdateDestroyAPIView,
)


urlpatterns = [
    path('api/vendors/', VendorListCreateAPIView.as_view(), name='vendor-list-create'),
    path('api/vendors/<int:pk>/', VendorRetrieveUpdateDestroyAPIView.as_view(), name='vendor-detail'),
    path('api/vendors/<int:pk>/performance/', VendorPerformanceAPIView.as_view(), name='vendor-performance'),
    path('api/historical-performance/', HistoricalPerformanceListCreateAPIView.as_view(), name='historical-performance-list-create'),
    path('api/historical-performance/<int:pk>/', HistoricalPerformanceRetrieveUpdateDestroyAPIView.as_view(), name='historical-performance-detail'),
]