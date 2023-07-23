from django.db import models


# Invoice models for the cheque out
class Invoice(models.Model):
    payment_method = models.CharField(max_length=4)
