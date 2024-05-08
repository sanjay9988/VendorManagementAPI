import django_filters
from django.db.models import JSONField
from .models import PurchaseOrder

class JSONFieldExactFilter(django_filters.CharFilter):
    def filter(self, qs, value):
        if value:
            qs = qs.filter(**{self.field_name: value})
        return qs

class PurchaseOrderFilter(django_filters.FilterSet):
    items = JSONFieldExactFilter(field_name='items')

    class Meta:
        model = PurchaseOrder
        fields = '__all__'
        filter_overrides = {
            JSONField: {
                'filter_class': JSONFieldExactFilter
            },
        }
