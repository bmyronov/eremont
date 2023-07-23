from django.contrib import admin

from repairshop.models import Customer


# Class to control how to display Customer on admin page
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone", "address"]
    list_display_links = ["name"]
    search_fields = ["name", "email", "phone", "address"]


# Register your model here.
admin.site.register(Customer, CustomerAdmin)
