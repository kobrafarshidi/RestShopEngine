from django.urls import path
from . import views

app_name = "products"

urlpatterns = [

    path("", views.product_list, name="product_list"),

    path("category/<slug:slug>/",
         views.category_products,
         name="category_products"),

    path("<int:pk>/",           # <--- این خط را تغییر بده از slug به int:pk
         views.product_detail,
         name="product_detail"),
]