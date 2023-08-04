from django.db import models


# Content that is shown on all the pages
class Content(models.Model):
    delivery_title = models.CharField(
        max_length=255, verbose_name="Заголовок в блоці ДОСТАВКА"
    )
    delivery_description = models.CharField(
        max_length=255, verbose_name="Текст в блоці ДОСТАВКА"
    )
    location = models.TextField(verbose_name="Посилання на локацію в google maps")

    def __str__(self):
        return "Контент, який відображається на усіх сторінках"

    class Meta:
        verbose_name = "Контент усіх сторінок"
        verbose_name_plural = "Контент усіх сторінок"
