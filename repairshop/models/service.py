from django.db import models

# from .service_sub_category import ServiceSubCategory
from .sub_category import SubCategory


# Services that the shop provides
class Service(models.Model):
    name = models.CharField(max_length=300, verbose_name="Назва")
    price = models.PositiveIntegerField(verbose_name="Ціна")
    position = models.PositiveIntegerField(default=0, verbose_name="Позиція в таблиці")
    sub_category = models.ManyToManyField(SubCategory, verbose_name="Підкатегорії")

    def __str__(self):
        return f"{self.name}: {self.price} грн."

    class Meta:
        verbose_name = "Послуга"
        verbose_name_plural = "Послуги"
        ordering = ["position", "name"]
