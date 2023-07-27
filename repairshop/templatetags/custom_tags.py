from django import template

register = template.Library()


@register.filter
def discount_price(price: int, discount: int) -> int:
    return int(price - price * discount / 100)
