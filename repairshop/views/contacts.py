from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Contacts page
def contacts(request: HttpRequest) -> HttpResponse:
    return render(request, "repairshop/contacts.html")
