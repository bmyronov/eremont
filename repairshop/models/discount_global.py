from django.db import models


# Contains information about current discount on the website
class DiscountGlobal(models.Model):
    name = models.CharField(max_length=255, verbose_name="Назва")
    percentage = models.IntegerField(verbose_name="Відсоток")
    final_date = models.DateField(null=True, blank=True, verbose_name="Кінцева дата")
    active = models.BooleanField(default=False, verbose_name="Ввімкнено")

    def __str__(self):
        return f"{self.name}: {self.percentage}%"

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
