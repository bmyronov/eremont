from django.db import models

from .order import Order
from .service import Service


# Contains all the services that belong to the current order
class OrderItem(models.Model):
    quantity = models.PositiveIntegerField(verbose_name="Кількість")
    price = models.PositiveIntegerField(verbose_name="Ціна")
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, verbose_name="Замовлення"
    )
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, verbose_name="Послуга"
    )

    class Meta:
        verbose_name = "Позиція для замовлення"
        verbose_name_plural = "Позиції для замовлення"
        ordering = ["-order", "service"]
