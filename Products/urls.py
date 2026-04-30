from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path("", views.product_list, name="product_list"),

    path("categories/", views.category_list, name="category_list"),  # ✅ اضافه کن

    path("category/<slug:slug>/", views.category_products, name="category_products"),
    path("<int:pk>/", views.product_detail, name="product_detail"),
]
