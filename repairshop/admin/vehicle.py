from typing import Any, List

from django.contrib import admin
from django.core.handlers.wsgi import WSGIRequest

from repairshop.models import Vehicle


# Class to control how to display Vehicle on admin page
class VehicleAdmin(admin.ModelAdmin):
    list_display = ["name", "customer"]
    list_display_links = ["name"]
    search_fields = ["name", "customer__name"]


# Register your model here.
admin.site.register(Vehicle, VehicleAdmin)
