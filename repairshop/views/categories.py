from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# All the services that repairshop provides
def categories(request: HttpRequest) -> HttpResponse:
    return render(request, "repairshop/categories.html")
