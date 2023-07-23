from django import forms
from django.utils.translation import gettext_lazy as _

from repairshop.models import Customer


# New order form
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["name", "phone", "email"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "type": "text",
                    "class": "mt-2 form-input rounded",
                    "id": "name",
                    "placeholder": "Ваше ім'я",
                    "oninvalid": 'setCustomValidity("Введіть своє ім\'я")',
                    "oninput": "setCustomValidity('')",
                }
            ),
            "phone": forms.TextInput(
                attrs={
                    "type": "text",
                    "class": "form-input rounded",
                    "id": "phone",
                    "placeholder": "Номер телефону",
                    "oninvalid": 'setCustomValidity("Введіть свій номер телефону")',
                    "oninput": "setCustomValidity('')",
                }
            ),
            "email": forms.TextInput(
                attrs={
                    "type": "email",
                    "class": "form-input rounded",
                    "id": "email",
                    "placeholder": "Email",
                    "oninvalid": 'setCustomValidity("Введіть свою електронну адресу")',
                    "oninput": "setCustomValidity('')",
                }
            ),
        }
        error_messages = {
            "name": {
                "max_length": _("Максимальна довжина 255 символів"),
                "invalid": _("Некоректно введене ім'я"),
            },
            "phone": {
                "invalid": _("Введіть коректний номер телефону."),
            },
            "email": {
                "invalid": _("Введіть коректну електронну адресу."),
            },
        }
