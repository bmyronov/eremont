from django.db import models


# Content of the main page (main page title etc)
class HomeContent(models.Model):
    title = models.CharField(max_length=255)
    banner_title = models.CharField(max_length=255)
    card_one_title = models.CharField(max_length=255)
    card_one_description = models.CharField(max_length=255)
    card_one_link = models.CharField(max_length=50)
    card_two_title = models.CharField(max_length=255)
    card_two_description = models.CharField(max_length=255)
    card_two_link = models.CharField(max_length=50)
    card_three_title = models.CharField(max_length=255)
    card_three_description = models.CharField(max_length=255)
    card_three_link = models.CharField(max_length=50)
    delivery_title = models.CharField(max_length=255)
    delivery_description = models.CharField(max_length=255)
    location = models.TextField()
