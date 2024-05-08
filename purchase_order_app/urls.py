from django.urls import path
from .views import (
    PurchaseOrderListCreateAPIView,
    PurchaseOrderRetrieveUpdateDestroyAPIView,
)
from .views import AcknowledgePurchaseOrderAPIView

urlpatterns = [
    path('api/purchase_orders/', PurchaseOrderListCreateAPIView.as_view(), name='purchase-order-list-create'),
    path('api/purchase_orders/<int:pk>/', PurchaseOrderRetrieveUpdateDestroyAPIView.as_view(), name='purchase-order-detail'),
    path('api/purchase_orders/<int:pk>/acknowledge/', AcknowledgePurchaseOrderAPIView.as_view(), name='acknowledge-purchase-order'),
]
