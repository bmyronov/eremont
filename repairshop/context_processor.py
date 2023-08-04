from django.http import HttpRequest

from repairshop.models import ContactInformation, Content, DiscountGlobal, SubCategory


# Header and Footer content
def contact_information(request: HttpRequest) -> dict:
    return {"contact_information": ContactInformation.objects.first()}


# Submenu for "послуги" tab in navbar
def sub_categories(request: HttpRequest) -> dict:
    return {"sub_categories": SubCategory.objects.all()}


# Content on all the pages
def content(request: HttpRequest) -> dict:
    return {"content": Content.objects.first()}


# DiscountGlobal
def discount(request: HttpRequest) -> dict:
    return {"discount": DiscountGlobal.objects.filter(active=True).first()}
