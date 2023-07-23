from django.db import models


# Contains information about current discount on the website
class DiscountGlobal(models.Model):
    name = models.CharField(max_length=255, verbose_name="Назва")
    percentage = models.IntegerField(verbose_name="Відсоток")
    active = models.BooleanField(default=False, verbose_name="Ввімкнено")

    def __str__(self):
        return self.name

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["active"],
                condition=models.Q(active="True"),
                name="Можлива лише одна активна знижка",
            )
        ]
        verbose_name = "Глобальна знижка"
        verbose_name_plural = "Глобальні знижки"
        ordering = ["active", "percentage", "name"]
