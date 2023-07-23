from django.db import models

from .customer import Customer
from .service import Service


# Model for personal discount (can contain discounts for some particular service price or
# for the whole price of the repair)
class DiscountPersonal(models.Model):
    name = models.CharField(max_length=255, verbose_name="Назва")
    percentage = models.IntegerField(verbose_name="Відсоток")
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, verbose_name="Клієнт"
    )
    service = models.ForeignKey(
        Service,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name="Послуга",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Персональна знижка"
        verbose_name_plural = "Персональні знижки"
        ordering = ["customer", "service"]
