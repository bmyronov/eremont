from typing import Any

from django.contrib import admin

from repairshop.models import DiscountPersonal, Order, OrderItem, OrderStatusHistory


# OrderItem inline
class OrderItemInline(admin.StackedInline):
    model = OrderItem
    fields = ["service", "quantity"]
    extra = 1


# Class to control how to display Order on admin page
class OrderAdmin(admin.ModelAdmin):
    list_display = ["customer", "vehicle", "order_status", "date"]
    list_display_links = ["customer"]
    list_editable = ["order_status"]
    list_filter = ["order_status", "date"]
    search_fields = ["customer__name", "order_status__name"]

    inlines = [OrderItemInline]

    # Auto generates new record in OrderStatusHistory when "order_status" has been changed
    def save_model(self, request, obj, form, change):
        field = "order_status"
        super().save_model(request, obj, form, change)

        if change and field in form.changed_data and form.cleaned_data.get(field):
            if str(obj.order_status) == "Виконано":
                discount_personal = DiscountPersonal.objects.filter(
                    customer=obj.customer,
                    service=None,
                    active=True,
                ).first()
                discount_personal.active = False
                discount_personal.save()

            OrderStatusHistory.objects.create(order=obj, order_status=obj.order_status)


# Register your model here.
admin.site.register(Order, OrderAdmin)
