from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from repairshop.forms import CustomerForm
from repairshop.models import (
    Customer,
    HomeContent,
    Order,
    OrderStatus,
    OrderStatusHistory,
    SubCategory,
)


# Create your views here.
def home(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = Customer.objects.filter(phone=form.cleaned_data["phone"]).first()
            if not customer:
                customer = form.save()

            order_status = OrderStatus.objects.get(name="Нове замовлення")
            order = Order.objects.create(customer=customer, order_status=order_status)
            order_status_history = OrderStatusHistory.objects.create(
                order=order, order_status=order_status
            )

            messages.success(
                request,
                f"<p>{customer.name}, Ваше замовлення прийнято! Наш оператор скоро зв'яжеться з вами!</p>\
                    <p>Для перевірки статусу ремонту, введіть свій номер телефону в пошуку в шапці сайту.</p>",
            )
            return redirect("home")
    else:
        form = CustomerForm()

    content = HomeContent.objects.get(pk=1)
    context = {
        "title": content.title,
        "content": content,
        "form": form,
    }
    return render(request, "repairshop/home.html", context=context)
