from django.contrib import admin
from django.db import models
from django.utils.html import format_html


# Order status model (adds options to choose the current status of the repair order)
class OrderStatus(models.Model):
    name = models.CharField(max_length=80, verbose_name="Статус")
    color = models.CharField(max_length=20, unique=True, verbose_name="Колір")

    @admin.display(description="")
    def colored_color_field(self):
        return format_html(
            '<span style="display: block; background-color: {}; width: 100%;">&nbsp;</span>',
            self.color,
        )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Статус замовлення"
        verbose_name_plural = "Статус замовлення"
        ordering = ["id"]
