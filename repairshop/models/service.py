from django.db import models

from .sub_category import SubCategory


# Services that the shop provides
class Service(models.Model):
    name = models.CharField(max_length=300, verbose_name="Назва")
    price = models.PositiveIntegerField(verbose_name="Ціна")
    sub_category = models.ManyToManyField(SubCategory, verbose_name="Підкатегорія")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Послуга"
        verbose_name_plural = "Послуги"
        ordering = ["sub_category__id", "name"]
