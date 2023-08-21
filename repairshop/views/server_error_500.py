from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Handles 500 "server error" error
def handler500(request: HttpRequest) -> HttpResponse:
    response = render(request, "repairshop/500.html")
    response.status_code = 500
    return response
