from django.contrib import admin

from repairshop.models import (
    ContactInformation,
    Customer,
    DiscountGlobal,
    DiscountPersonal,
    HomeContent,
    Order,
    OrderStatus,
    OrderStatusHistory,
    Service,
)

# Register your models here.
admin.site.register(ContactInformation)
admin.site.register(HomeContent)
admin.site.register(Customer)
admin.site.register(Service)
admin.site.register(DiscountGlobal)
admin.site.register(DiscountPersonal)
admin.site.register(OrderStatus)
admin.site.register(OrderStatusHistory)
admin.site.register(Order)
