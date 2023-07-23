from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# About us page
def about(request: HttpRequest) -> HttpResponse:
    return render(request, "repairshop/about.html")
