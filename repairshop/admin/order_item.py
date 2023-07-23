from django.contrib import admin

from repairshop.models import OrderItem


# Class to control how to display OrderItem on admin page
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ["order", "service", "quantity", "price"]
    list_display_links = ["order"]
    search_fields = ["order", "service"]


# Register your model here.
admin.site.register(OrderItem, OrderItemAdmin)
