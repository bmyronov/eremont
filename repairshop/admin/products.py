from django.contrib import admin

from repairshop.models import Product


# Class to control how to display Product on admin page
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "product_code", "price", "price_blank", "url", "photo"]
    list_display_links = ["name"]
    list_editable = ["price_blank"]
    search_fields = ["name", "product_code", "price"]
    list_filter = ["price_blank"]
    prepopulated_fields = {"url": ["product_code", "name"]}


# Register your model here.
admin.site.register(Product, ProductAdmin)
