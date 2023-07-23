from django.db import models

from .order import Order
from .order_status import OrderStatus


# History of the current order status changes
class OrderStatusHistory(models.Model):
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата")
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, verbose_name="Замовлення"
    )
    order_status = models.ForeignKey(
        OrderStatus, on_delete=models.RESTRICT, verbose_name="Статус замовлення"
    )

    class Meta:
        verbose_name = "Історія замовлення"
        verbose_name_plural = "Історія замовлення"
        ordering = ["order", "-date"]
