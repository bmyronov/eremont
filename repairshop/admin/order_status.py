from django.contrib import admin
from django.utils.html import format_html

from repairshop.models import OrderStatus


# Class to control how to display OrderStatus on admin page
class OrderStatusAdmin(admin.ModelAdmin):
    list_display = ["name", "colored_color_field", "color"]
    list_display_links = ["name"]
    list_editable = ["color"]
    search_fields = ["name", "color"]


# Register your model here.
admin.site.register(OrderStatus, OrderStatusAdmin)
