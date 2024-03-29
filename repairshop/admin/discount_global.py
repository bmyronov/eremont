from django.contrib import admin

from repairshop.models import DiscountGlobal


# Class to control how to display DiscountGlobal on admin page
class DiscountGlobalAdmin(admin.ModelAdmin):
    list_display = ["name", "percentage", "final_date", "active"]
    list_display_links = ["name"]
    list_editable = ["active"]
    list_filter = ["active"]
    search_fields = ["name", "percentage", "final_date"]


# Register your model here.
admin.site.register(DiscountGlobal, DiscountGlobalAdmin)
