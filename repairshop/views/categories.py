from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from repairshop.models import HomeContent


# All the services that repairshop provides
def categories(request: HttpRequest) -> HttpResponse:
    location = HomeContent.objects.get(pk=1).location
    return render(
        request,
        "repairshop/categories.html",
        {
            "location": location,
        },
    )
