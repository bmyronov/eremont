from django.contrib import admin

from repairshop.models import HomeContent


# Class to control how to display HomeContent on admin page
class HomeContentAdmin(admin.ModelAdmin):
    list_display = ["title"]
    list_display_links = ["title"]


# Register your model here.
admin.site.register(HomeContent, HomeContentAdmin)
