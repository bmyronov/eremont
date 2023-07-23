from django.contrib import admin

from repairshop.models import SubCategory


# Class to control how to display SubCategory on admin page
class SubCategoriesAdmin(admin.ModelAdmin):
    list_display = ["name", "url", "position", "image", "blank"]
    list_display_links = ["name"]
    list_editable = ["position"]
    search_fields = ["name", "position"]
    prepopulated_fields = {"url": ["name"]}


# Register your model here.
admin.site.register(SubCategory, SubCategoriesAdmin)
