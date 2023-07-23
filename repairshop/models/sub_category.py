from django.db import models
from django.urls import reverse


# Categories that are shown in "послуги"
class SubCategory(models.Model):
    name = models.CharField(max_length=255, blank=True, verbose_name="Назва")
    url = models.SlugField(
        max_length=255, unique=True, db_index=True, blank=True, verbose_name="URL"
    )
    position = models.PositiveIntegerField(verbose_name="Позиція", default=1)
    image = models.ImageField(
        upload_to="images/sub_categories/",
        default=None,
        blank=True,
        verbose_name="Малюнок",
    )
    blank = models.BooleanField(default=False, verbose_name="Розділювальна лінія")

    def get_absolute_url(self):
        return reverse("sub_category", kwargs={"sub_category": self.url})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Підкатегорія"
        verbose_name_plural = "Підкатегорії"
        ordering = ["position"]
