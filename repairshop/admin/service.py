from django.contrib import admin

from repairshop.models import Service


# Class to control how to display Service on admin page
class ServiceAdmin(admin.ModelAdmin):
    model = Service

    list_display = ["name", "price", "position"]
    list_display_links = ["name"]
    list_editable = ["position"]
    list_filter = ["sub_category"]
    search_fields = ["name", "price", "sub_category__name"]
    filter_horizontal = ["sub_category"]

    class Meta:
        model = Service


# Register your model here.
admin.site.register(Service, ServiceAdmin)
