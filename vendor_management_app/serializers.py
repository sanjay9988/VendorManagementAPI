from rest_framework import serializers
from .models import Vendor, HistoricalPerformance




class VendorStatisticsSerializer(serializers.Serializer):
    on_time_delivery_rate = serializers.FloatField()
    quality_rating_average = serializers.FloatField()
    average_response_time = serializers.FloatField()
    fulfillment_rate = serializers.FloatField()

    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     for key, value in data.items():
    #         if isinstance(value, float):
    #             data[key] = round(value, 2)  # Limit to 2 decimal places
    #     return data

    

class VendorSerializer(serializers.ModelSerializer):
    vendor_code = serializers.CharField(required=False)
    class Meta:
        model = Vendor
        fields = ['id','name', 'contact_details', 'address', 'vendor_code'] 
        
    

class HistoricalPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalPerformance
        fields = '__all__'
