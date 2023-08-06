from repairshop.models import (
    ContactInformation,
    Content,
    HomeContent,
    OrderStatus,
    SubCategory,
)


# Writes default website data info db
def main():
    if not ContactInformation.objects.all():
        ContactInformation.objects.create(
            address="вул. Складська 24",
            phone_number_one="0683101210",
            phone_number_two="0733101210",
            weekday_start="Пн",
            weekday_end="Пн",
            dayoff_start="Нд",
            hours_start="10:00",
            hours_end="18:00",
        )

    HomeContent.objects.update_or_create(
        title="Ремонт електросамокатів в місті Вінниця",
        banner_title="Ремонт електросамокатів <br> в місті Вінниця",
        card_one_title="Швидкiсть",
        card_one_description="Швидкiсть",
        card_one_link="about",
        card_two_title="Якiсть",
        card_two_description="Якiсть",
        card_two_link="about",
        card_three_title="Доступна цiна",
        card_three_description="Доступна цiна",
        card_three_link="categories",
    )

    Content.objects.update_or_create(
        delivery_title="Якщо Ви не можете приїхати <br> до нас, то ми їдемо до вас",
        delivery_description="Заповніть заявку на сайті або пишить у наш телеграмм бот",
        location='<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d1302.1770252386123!2d28.523771658721923!3d49.2507349!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x472d5b33159b5349%3A0x224f94568fcd1816!2sSkladska%20St%2C%2024%2C%20Vinnytsia%2C%20Vinnyts&#39;ka%20oblast%2C%2021000!5e0!3m2!1sen!2sua!4v1687719646018!5m2!1sen!2sua" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>',
    )

    SubCategory.objects.update_or_create(
        name="Ремонт елктросамокатів", url="electro-scootes", position=1, blank=False
    )
    SubCategory.objects.update_or_create(
        name="Ремонт електровелосипедів", url="electro-bikes", position=2, blank=False
    )
    SubCategory.objects.update_or_create(name="", url="", position=3, blank=True)
    SubCategory.objects.update_or_create(
        name="Ремонт велосипедів", url="bikes", position=4, blank=False
    )

    OrderStatus.objects.update_or_create(name="Нове замовлення", color="#5bc0de")
    OrderStatus.objects.update_or_create(
        name="Опрацьований оператором", color="#0275d8"
    )
    OrderStatus.objects.update_or_create(name="Прийнято на ремонт", color="#f7e463")
    OrderStatus.objects.update_or_create(name="Очікує клієнта", color="#f0ad4e")
    OrderStatus.objects.update_or_create(name="Виконано", color="#5cb85c")
    OrderStatus.objects.update_or_create(name="Скасовано", color="#d9534f")
