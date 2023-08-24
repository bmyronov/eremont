from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from repairshop.models import Product


# Product page
def product(request: HttpRequest, product_url: str) -> HttpResponse:
    product = Product.objects.get(url=product_url)

    context = {
        "name": product.name,
        "product_code": product.product_code,
        "photo": product.photo,
        "price": product.price,
        "price_blank": product.price_blank,
        "description": product.description,
    }
    return render(request, "repairshop/product.html", context=context)
