from ckeditor.fields import RichTextField
from django.db import models


def photo_path(instance, filename):
    return "images/products/{0}/{1}".format(instance.product_code, filename)


# Product model
class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Назва товару")
    product_code = models.CharField(max_length=10, verbose_name="Код товару")
    price = models.PositiveIntegerField(default=0, verbose_name="Ціна")
    price_blank = models.BooleanField(default=False, verbose_name="Без ціни")
    photo = models.ImageField(
        upload_to=photo_path,
        default=None,
        blank=True,
        verbose_name="Фото товару",
    )
    url = models.SlugField(
        max_length=255, unique=True, db_index=True, blank=True, verbose_name="URL"
    )
    description = RichTextField(verbose_name="Опис")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товари"
