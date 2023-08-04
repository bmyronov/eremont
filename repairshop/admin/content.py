from django.contrib import admin

from repairshop.models import Content


# Class to control how to display Content on admin page
class ContentAdmin(admin.ModelAdmin):
    list_display = ["delivery_title", "delivery_description", "location"]
    list_display_links = ["delivery_title"]


# Register your model here.
admin.site.register(Content, ContentAdmin)
