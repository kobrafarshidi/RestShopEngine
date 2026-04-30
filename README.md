# 🛍️ Django Shop (RestShopEngine)

> فروشگاه اینترنتی با **Django + DRF + PostgreSQL** | مناسب برای توسعه و مقیاس‌پذیری

[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue)](https://www.postgresql.org/)
[![DRF](https://img.shields.io/badge/DRF-3.15-red)](https://www.django-rest-framework.org/)

---

## 🚀 امکانات

- مدیریت محصول و دسته‌بندی (پنل ادمین)
- ثبت‌نام و احراز هویت کاربران
- سبد خرید و ثبت سفارش
- پرداخت شبیه‌سازی‌شده
- API کامل با DRF

---

## 🛠️ تکنولوژی‌ها

`Django Rest Framework(DRF)` • `PostgreSQL` • `HTML/CSS/JS`

---

## ⚡ نصب سریع

```bash
git clone https://github.com/kobrafarshidi/RestShopEngine.git
cd django-shop
python -m venv venv
source venv/bin/activate 
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
