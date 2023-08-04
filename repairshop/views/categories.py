from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from repairshop.models import HomeContent


# All the services that repairshop provides
def categories(request: HttpRequest) -> HttpResponse:
    context = {"title": "Послуги"}
    return render(request, "repairshop/categories.html", context=context)
