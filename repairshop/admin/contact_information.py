from django.contrib import admin

from repairshop.models import ContactInformation


# Class to control how to display ContactInformation on admin page
class ContactInformationAdmin(admin.ModelAdmin):
    list_display = ["address", "phone_number_one", "phone_number_two"]
    list_display_links = ["address"]


# Register your model here.
admin.site.register(ContactInformation, ContactInformationAdmin)
