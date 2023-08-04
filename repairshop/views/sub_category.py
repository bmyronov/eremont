from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from repairshop.models import DiscountGlobal, Service, SubCategory


# View for every category in Category table
def sub_category(request: HttpRequest, sub_category: str) -> HttpResponse:
    sub_category = SubCategory.objects.filter(url=sub_category).first()
    services = Service.objects.filter(sub_category=sub_category).all()

    context = {
        "title": sub_category.name,
        "sub_category": sub_category,
        "services": services,
    }
    return render(request, "repairshop/sub_category.html", context=context)
