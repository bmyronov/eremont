from typing import Any

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Handles 404 "page not found" error
def handler404(request: HttpRequest, exception: Any) -> HttpResponse:
    response = render(request, "repairshop/404.html")
    response.status_code = 404
    return response
