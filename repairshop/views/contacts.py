from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from repairshop.models import Contact


# Contacts page
def contacts(request: HttpRequest) -> HttpResponse:
    about = Contact.objects.first()

    context = {
        "title": about.title,
        "description": about.description,
    }
    return render(request, "repairshop/contacts.html", context=context)
