from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from repairshop.models import SubCategory


# View for every category in Category table
def sub_category(request: HttpRequest, sub_category: str) -> HttpResponse:
    sub_category = SubCategory.objects.filter(url=sub_category).first()
    return render(
        request, "repairshop/sub_category.html", {"sub_category": sub_category}
    )
