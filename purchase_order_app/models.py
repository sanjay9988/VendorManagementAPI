from django.db import models
from django.utils import timezone
from purchase_order_app.utils import generate_unique_po_number
from vendor_management_app.models import Vendor
from .choices import PURCHASE_ORDER_STATUS_CHOICES
from django.db.models import Sum,Avg


from django.db.models.signals import post_save
from django.dispatch import receiver



class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=20, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField(default=timezone.now) 
    delivery_date = models.DateTimeField(null=True, blank=True)
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, choices=PURCHASE_ORDER_STATUS_CHOICES,default="pending")
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField(default=timezone.now)
    acknowledgment_date = models.DateTimeField(null=True, blank=True)
    
    def save(self, *args, **kwargs):

        if self.pk:
            previous_status = PurchaseOrder.objects.get(pk=self.pk).status
            if self.status != previous_status:
                fulfilment_rate = self.calculate_fulfilment_rate()
                self.vendor.fulfillment_rate = fulfilment_rate
                self.vendor.save()

        if self.acknowledgment_date is not None and self.pk:
            average_response_time = self.calculate_average_response_time()
            self.vendor.average_response_time = average_response_time
            self.vendor.save()

        if self.quality_rating is not None and self.pk:
            quality_rating_average = self.calculate_quality_rating_average()
            self.vendor.quality_rating_average = quality_rating_average
            self.vendor.save()

        if self.status == 'completed' and self.pk:
            on_time_delivery_rate = self.calculate_on_time_delivery_rate()
            self.vendor.on_time_delivery_rate = on_time_delivery_rate
            self.vendor.save()

        if not self.quantity:
            total_quantity = sum(item.get('quantity', 0) for item in self.items)
            self.quantity = total_quantity

        if not self.po_number:
            self.po_number = generate_unique_po_number()

        if not self.issue_date:
            self.issue_date = timezone.now()
        super(PurchaseOrder, self).save(*args, **kwargs)

    def __str__(self):
        return self.po_number
    
    def calculate_on_time_delivery_rate(self):
        completed_orders = PurchaseOrder.objects.filter(vendor=self.vendor, status='completed')
        total_completed_orders = completed_orders.count()
        on_time_deliveries = completed_orders.filter(delivery_date__lte=timezone.now()).count()
        if total_completed_orders == 0:
            return 0
        return (on_time_deliveries / total_completed_orders) * 100
    
    def calculate_quality_rating_average(self):
        completed_orders = PurchaseOrder.objects.filter(vendor=self.vendor, status='completed').exclude(quality_rating__isnull=True)
        total_completed_orders = completed_orders.count()

        if total_completed_orders == 0:
            return 0
        quality_ratings = completed_orders.aggregate(total_rating=Sum('quality_rating'))['total_rating']
        return quality_ratings / total_completed_orders
    
    def calculate_average_response_time(self):
        acknowledged_orders = PurchaseOrder.objects.filter(vendor=self.vendor, acknowledgment_date__isnull=False)
        total_acknowledged_orders = acknowledged_orders.count()
        if total_acknowledged_orders == 0:
            return None
        total_response_time = 0
        for order in acknowledged_orders:
            response_time = (order.acknowledgment_date - order.issue_date).total_seconds()
            total_response_time += response_time
        average_response_time = total_response_time / total_acknowledged_orders
        return average_response_time
    
    def calculate_fulfilment_rate(self):
        total_orders = PurchaseOrder.objects.filter(vendor=self.vendor).count()
        if total_orders == 0:
            return None
        successfully_fulfilled_orders = PurchaseOrder.objects.filter(vendor=self.vendor, status='completed', quality_rating__isnull=False).count()
        fulfilment_rate = (successfully_fulfilled_orders / total_orders) * 100
        return fulfilment_rate

