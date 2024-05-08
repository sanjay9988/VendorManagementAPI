
from vendor_management_app.utils import generate_unique_vendor_number
from django.db import models


class Vendor(models.Model):
    name = models.CharField(max_length=100)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=20)
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_average = models.FloatField(default=0)
    average_response_time = models.FloatField(default=0,blank=True,null=True)
    fulfillment_rate = models.FloatField(default=0)

    def save(self, *args, **kwargs):
        if not self.vendor_code:
            self.vendor_code = generate_unique_vendor_number()
        super(Vendor, self).save(*args, **kwargs)


    def __str__(self):
        return self.name

class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey('vendor_management_app.Vendor', on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self):
        return f"{self.vendor.name} - {self.date}"