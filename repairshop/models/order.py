from django.db import models

from .customer import Customer
from .order_status import OrderStatus
from .vehicle import Vehicle


# Order model
class Order(models.Model):
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, verbose_name="Клієнт"
    )
    order_status = models.ForeignKey(
        OrderStatus, on_delete=models.RESTRICT, verbose_name="Статус замовлення"
    )
    vehicle = models.ForeignKey(
        Vehicle,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name="Транспортний засіб",
    )

    class Meta:
        verbose_name = "Замовлення"
        verbose_name_plural = "Замовлення"
        ordering = ["-date"]
