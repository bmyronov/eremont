from django.db import models

from .order import Order


# Additional expenses like tire, gas handle etc
class AdditionExpense(models.Model):
    name = models.CharField(max_length=255, verbose_name="Назва")
    price = models.PositiveIntegerField(verbose_name="Ціна")
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, verbose_name="Замовлення"
    )

    def __str__(self):
        return f"{self.name}: {self.price} грн."

    class Meta:
        verbose_name = "Додаткова витрата"
        verbose_name_plural = "Додаткові витрати"
        ordering = ["-id"]
