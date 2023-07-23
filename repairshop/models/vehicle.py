from django.db import models

from .customer import Customer


# Vehicles info
class Vehicle(models.Model):
    name = models.CharField(max_length=255, verbose_name="Назва")
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, verbose_name="Власник"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Транспортний засіб"
        verbose_name_plural = "Транспортні засоби"
        ordering = ["customer"]
