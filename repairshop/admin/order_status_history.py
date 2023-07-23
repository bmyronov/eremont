from django.contrib import admin

from repairshop.models import OrderStatusHistory


# Class to control how to display OrderStatusHistory on admin page
class OrderStatusHistoryAdmin(admin.ModelAdmin):
    list_display = ["order_id", "order_status"]
    list_display_links = None
    list_filter = ["order_status", "date"]
    search_fields = ["order__id", "order_status__name"]


# Register your model here.
admin.site.register(OrderStatusHistory, OrderStatusHistoryAdmin)
