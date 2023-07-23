from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Customer data that stores in db
class Customer(models.Model):
    name = models.CharField(max_length=255, verbose_name="Ім'я")
    email = models.EmailField(verbose_name="Email")
    phone = PhoneNumberField(region="UA", verbose_name="Телефон")
    address = models.CharField(max_length=255, blank=True, verbose_name="Адреса")

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Клієнт"
        verbose_name_plural = "Клієнти"
        ordering = ["-id"]
