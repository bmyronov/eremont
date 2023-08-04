from django.contrib import admin

from repairshop.models import About


# Class to control how to display Content on admin page
class AboutAdmin(admin.ModelAdmin):
    list_display = ["title"]
    list_display_links = ["title"]


# Register your model here.
admin.site.register(About, AboutAdmin)
