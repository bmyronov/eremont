from django.contrib import admin

from repairshop.models import DiscountPersonal


# Class to control how to display DiscountPersonal on admin page
class DiscountPersonalAdmin(admin.ModelAdmin):
    list_display = ["name", "percentage", "customer", "service", "active"]
    list_display_links = ["name"]
    list_editable = ["percentage", "active"]
    list_filter = ["active"]
    search_fields = ["name", "percentage", "customer", "service"]


# Register your model here.
admin.site.register(DiscountPersonal, DiscountPersonalAdmin)
