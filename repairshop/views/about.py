from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from repairshop.models import About


# About us page
def about(request: HttpRequest) -> HttpResponse:
    about = About.objects.first()

    context = {
        "title": about.title,
        "description": about.description,
    }
    return render(request, "repairshop/about.html", context=context)
