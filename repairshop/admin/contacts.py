from django.contrib import admin

from repairshop.models import Contact


# Class to control how to display Content on admin page
class ContactAdmin(admin.ModelAdmin):
    list_display = ["title"]
    list_display_links = ["title"]


# Register your model here.
admin.site.register(Contact, ContactAdmin)
