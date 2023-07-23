from django.db import models


# Content of the main page (main page title etc)
class HomeContent(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    banner_title = models.CharField(max_length=255, verbose_name="Текст в банері")
    card_one_title = models.CharField(max_length=255, verbose_name="Заголовок картки 1")
    card_one_description = models.CharField(
        max_length=255, verbose_name="Опис картки 1"
    )
    card_one_link = models.CharField(max_length=50, verbose_name="Посилання картки 1")
    card_two_title = models.CharField(max_length=255, verbose_name="Заголовок картки 2")
    card_two_description = models.CharField(
        max_length=255, verbose_name="Опис картки 2"
    )
    card_two_link = models.CharField(max_length=50, verbose_name="Посилання картки 2")
    card_three_title = models.CharField(
        max_length=255, verbose_name="Заголовок картки 3"
    )
    card_three_description = models.CharField(
        max_length=255, verbose_name="Опис картки 3"
    )
    card_three_link = models.CharField(max_length=50, verbose_name="Посилання картки 3")
    delivery_title = models.CharField(
        max_length=255, verbose_name="Заголовок в блоці ДОСТАВКА"
    )
    delivery_description = models.CharField(
        max_length=255, verbose_name="Текст в блоці ДОСТАВКА"
    )
    location = models.TextField(verbose_name="Посилання на локацію в google maps")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Головна сторінка"
        verbose_name_plural = "Головна сторінка"
