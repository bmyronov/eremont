from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# All the contacts on the web page (phone numbers, address, social nerwork links etc)
class ContactInformation(models.Model):
    address = models.CharField(max_length=255, verbose_name="Адреса")
    phone_number_one = PhoneNumberField(
        region="UA", blank=False, verbose_name="Номер телефону 1"
    )
    phone_number_two = PhoneNumberField(
        region="UA", blank=True, verbose_name="Номер телефону 2"
    )
    telegram_link = models.CharField(
        max_length=255, default="#", verbose_name="Telegram"
    )
    instagram_link = models.CharField(
        max_length=255, default="#", verbose_name="Instagram"
    )
    weekday_start = models.CharField(max_length=2, verbose_name="Початок вихідних")
    weekday_end = models.CharField(max_length=2, verbose_name="Кінець вихідних")
    dayoff_start = models.CharField(max_length=2, verbose_name="Початок робочого тижня")
    dayoff_end = models.CharField(
        max_length=2, blank=True, verbose_name="Кінець робочого тижня"
    )
    hours_start = models.CharField(
        max_length=5, verbose_name="Початок робочого дня (години нап. 10:00)"
    )
    hours_end = models.CharField(
        max_length=5, verbose_name="Кінець робочого дня (години нап. 18:00)"
    )

    class Meta:
        verbose_name = "Контактна інформація сайту"
        verbose_name_plural = "Контактна інформація сайту"
