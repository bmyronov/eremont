from django.http import HttpRequest

from repairshop.models import ContactInformation, SubCategory


# Header and Footer content
def contact_information(request: HttpRequest) -> dict:
    return {"contact_information": ContactInformation.objects.get(pk=1)}


# Submenu for "послуги" tab in navbar
def sub_categories(request: HttpRequest) -> dict:
    return {"sub_categories": SubCategory.objects.all()}
