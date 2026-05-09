# 🛍️ Django Shop (RestShopEngine)

> فروشگاه اینترنتی با **Django + DRF + PostgreSQL** | مناسب برای توسعه و مقیاس‌پذیری

[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue)](https://www.postgresql.org/)
[![DRF](https://img.shields.io/badge/DRF-3.15-red)](https://www.django-rest-framework.org/)

---
## 🚀 امکانات

<div align="center">
  <table>
    <tr align="center">
      <td>
        <img src="static/images/admin.png" alt="مدیریت محصول" width="130" height="95" style="border-radius: 10px; object-fit: cover;">
        <br />
        <strong>مدیریت محصول</strong><br />
        <sub>(پنل ادمین)</sub>
      </td>
      <td>
        <img src="static/images/products.jpg" alt="محصولات" width="130" height="95" style="border-radius: 10px; object-fit: cover;">
        <br />
        <strong>محصولات</strong><br />
        <sub>(دسته‌بندی)</sub>
      </td>
      <td>
        <img src="static/images/cart.jpg" alt="سبد خرید" width="130" height="95" style="border-radius: 10px; object-fit: cover;">
        <br />
        <strong>سبد خرید</strong>
      </td>
      <td>
        <img src="static/images/order.png" alt="ثبت سفارش" width="130" height="95" style="border-radius: 10px; object-fit: cover;">
        <br />
        <strong>ثبت سفارش</strong>
      </td>
      <td>
        <img src="static/images/main.png" alt="صفحه اصلی" width="130" height="95" style="border-radius: 10px; object-fit: cover;">
        <br />
        <strong>صفحه اصلی</strong><br />
        
      </td>
    </table>
    <tr align="center">
      <td colspan="5">
        <strong>🔐 ثبت‌نام و احراز هویت + 💳 پرداخت شبیه‌سازی‌شده + ✨ API کامل با DRF</strong>
      </td>
    </tr>
  </table>
</div>

---

## 🛠️ تکنولوژی‌ها

`Django Rest Framework(DRF)` • `PostgreSQL` • `HTML/CSS/JS`

---

## ⚡ نصب سریع

```bash
git clone https://github.com/kobrafarshidi/RestShopEngine.git
cd RestShopEngine
python -m venv venv
source venv/bin/activate  # در ویندوز: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
