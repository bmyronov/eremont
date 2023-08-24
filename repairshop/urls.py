from django.urls import path

from repairshop import views

urlpatterns = [
    path("", views.home, name="home"),
    path("categories/<slug:sub_category>/", views.sub_category, name="sub_category"),
    path("about/", views.about, name="about"),
    path("categories/", views.categories, name="categories"),
    path("contacts/", views.contacts, name="contacts"),
    path("products/<slug:product_url>/", views.product, name="product"),
]
