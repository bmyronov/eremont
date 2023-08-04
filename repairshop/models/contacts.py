from ckeditor.fields import RichTextField
from django.db import models


# Contact page data
class Contact(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    description = RichTextField(verbose_name="Опис")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Контакти"
        verbose_name_plural = "Контакти"
