from django.contrib import admin

from repairshop.models import Service


# Class to control how to display Service on admin page
class ServiceAdmin(admin.ModelAdmin):
    list_display = ["name", "price"]
    list_display_links = ["name"]
    list_filter = ["sub_category"]
    search_fields = ["name", "price", "sub_category__name"]


# Register your model here.
admin.site.register(Service, ServiceAdmin)
