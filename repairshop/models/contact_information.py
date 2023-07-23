from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# All the contacts on the web page (phone numbers, address, social nerwork links etc)
class ContactInformation(models.Model):
    address = models.CharField(max_length=255)
    phone_number_one = PhoneNumberField(region="UA", blank=False)
    phone_number_two = PhoneNumberField(region="UA", blank=True)
    telegram_link = models.CharField(max_length=255, default="#")
    instagram_link = models.CharField(max_length=255, default="#")
    weekday_start = models.CharField(max_length=2)
    weekday_end = models.CharField(max_length=2)
    dayoff_start = models.CharField(max_length=2)
    dayoff_end = models.CharField(max_length=2, blank=True)
    hours_start = models.CharField(max_length=2)
    hours_end = models.CharField(max_length=2)
