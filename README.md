# 🛍️ Django Shop

> فروشگاه اینترنتی با **Django + DRF + PostgreSQL** | مناسب برای توسعه و مقیاس‌پذیری

[![Django](https://img.shields.io/badge/Django-5.x-green)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/DRF-3.15-red)](https://www.django-rest-framework.org/)

---

## 🚀 امکانات

- مدیریت محصول و دسته‌بندی (پنل ادمین)
- ثبت‌نام و احراز هویت کاربران
- سبد خرید و ثبت سفارش
- پرداخت شبیه‌سازی‌شده
- API کامل با DRF

---

## 📽️ فیلم‌های آموزشی 

| فیلم | توضیح |
|------|-------|
| [مدیریت محصول و دسته‌بندی](./docs/admin.mp4) | اضافه کردن، ویرایش و حذف محصولات توسط ادمین |
| [فرایند کاربر](./docs/user.mp4) | ثبت‌نام → افزودن به سبد → ثبت سفارش → پرداخت |

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
