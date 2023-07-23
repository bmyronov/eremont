from repairshop.models import ContactInformation, HomeContent, SubCategory


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
            hours_start="10",
            hours_end="18",
        )

    HomeContent.objects.update_or_create(
        title="Ремонт електросамокатів в місті Вінниця",
        banner_title="Ремонт електросамокатів <br> в місті Вінниця",
        delivery_title="Якщо Ви не можете приїхати <br> до нас, то ми їдемо до вас",
        delivery_description="Лишайте заявку або пишить у наш телеграмм бот",
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


if __name__ == "__main__":
    main()
