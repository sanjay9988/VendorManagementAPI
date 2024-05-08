from rest_framework import serializers
from .models import PurchaseOrder
from django.utils import timezone

class PurchaseOrderSerializer(serializers.ModelSerializer):
    po_number = serializers.CharField(required=False)
    status = serializers.CharField(required=False)
    delivery_date=serializers.DateTimeField(required=False, input_formats=['%Y-%m-%dT%H:%M:%S'])

    class Meta:
        model = PurchaseOrder
        fields = '__all__'
        read_only_fields=["id","order_date","issue_date","acknowledgment_date","quantity","po_number"]
    
    def validate_delivery_date(self, value):
        """
        Validate that the delivery_date is not in the past.
        """
        if value < timezone.now():
            raise serializers.ValidationError("Delivery date cannot be in the past.")
        return value
    



