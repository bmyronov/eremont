from typing import Any

from django.db import models

from .discount_global import DiscountGlobal
from .discount_personal import DiscountPersonal
from .order import Order
from .service import Service


# Contains all the services that belong to the current order
class OrderItem(models.Model):
    quantity = models.PositiveIntegerField(default=1, verbose_name="Кількість")
    price = models.PositiveIntegerField(default=1, verbose_name="Ціна")
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, verbose_name="Замовлення"
    )
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, verbose_name="Послуга"
    )

    # Calculates the price with discounts
    def set_price(self) -> None:
        discount_global = DiscountGlobal.objects.filter(active=True).first()
        discount_for_service = DiscountPersonal.objects.filter(
            customer=self.order.customer, service=self.service, active=True
        ).first()
        discount_personal = DiscountPersonal.objects.filter(
            customer=self.order.customer, service=None, active=True
        ).first()

        print("DiscountGlobal:", discount_global)
        print("discount_for_service:", discount_for_service)
        print("discount_personal:", discount_personal)

        # If no discounts available
        if not discount_for_service and not discount_personal and not discount_global:
            self.price = self.service.price * self.quantity
            print("# If no discounts available")
            return None

        # If only discount_global
        if not discount_for_service and not discount_personal:
            service_price = int(
                self.service.price
                - self.service.price * discount_global.percentage / 100
            )
            self.price = service_price * self.quantity
            print("# If only discount_global")
            return None

        # If discount_for_service or discount_personal
        if not discount_global:
            print("# No discount_global")
            if discount_for_service:
                service_price = int(
                    self.service.price
                    - self.service.price * discount_for_service.percentage / 100
                )
                discount_for_service.active = False
                discount_for_service.save()

                # If the quantity is > 1 discount is calculated only for 1 service
                if not self.quantity <= 1:
                    quantity = self.quantity - 1
                    self.price = service_price + self.service.price * quantity
                    print("# If discount_for_service 100")
                    return None

                self.price = service_price
                print("# If discount_for_service")
                return None

            if discount_personal:
                service_price = int(
                    self.service.price
                    - self.service.price * discount_personal.percentage / 100
                )
                self.price = service_price * self.quantity
                print("# If discount_personal")
                return None

        if discount_global and (discount_for_service or discount_personal):
            if discount_for_service:
                if (
                    discount_global.percentage + discount_for_service.percentage
                ) >= 100:
                    # If the quantity is 1 the price is 0
                    if self.quantity == 1:
                        self.price = 0
                        discount_for_service.active = False
                        discount_for_service.save()
                        return None

                    # If the quantity is > 1
                    service_price = int(
                        self.service.price
                        - self.service.price * discount_global.percentage / 100
                    )
                    quantity = self.quantity - 1
                    self.price = self.service.price * quantity
                    discount_for_service.active = False
                    discount_for_service.save()
                    return None

                service_price = int(
                    self.service.price
                    - self.service.price
                    * (discount_global.percentage + discount_for_service.percentage)
                    / 100
                )
                discount_for_service.active = False
                discount_for_service.save()
                # If the quantity is > 1
                if self.quantity > 1:
                    quantity = self.quantity - 1
                    self.price = int(
                        service_price
                        + (
                            self.service.price
                            * discount_global.percentage
                            / 100
                            * quantity
                        )
                    )
                    return None

                self.price = service_price
                return None

            if discount_personal:
                if (discount_global.percentage + discount_personal.percentage) >= 100:
                    # If the quantity is 1 the price is 0
                    if self.quantity == 1:
                        self.price = 0
                        return None

                    service_price = (
                        self.service.price
                        - self.service.price * discount_global.percentage / 100
                    )
                    quantity = self.quantity - 1
                    self.price = service_price * quantity
                    return None

                service_price = int(
                    self.service.price
                    - self.service.price
                    * (discount_global.percentage + discount_personal.percentage)
                    / 100
                )
                # If the quantity is > 1
                if self.quantity > 1:
                    quantity = self.quantity - 1
                    self.price = int(
                        service_price
                        + (
                            self.service.price
                            * discount_global.percentage
                            / 100
                            * quantity
                        )
                    )
                    return None

                self.price = service_price
                return None

    def save(self, *args: Any, **kwargs: Any):
        self.set_price()
        super(OrderItem, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.service.name} x{self.quantity} - {self.price} грн (зі знижкою)"

    class Meta:
        verbose_name = "Позиція для замовлення"
        verbose_name_plural = "Позиції для замовлення"
        ordering = ["-order", "service"]
