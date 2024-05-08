
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('vendor_management_app.urls')),
    path('', include('purchase_order_app.urls')),
]
