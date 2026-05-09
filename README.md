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
        <img src="static/images/admin.png" alt="مدیریت محصول و دسته‌بندی" width="140" height="100" style="border-radius: 10px; object-fit: cover;">
        <br />
        <strong>مدیریت محصول و دسته‌بندی</strong><br />
        <sub>(پنل ادمین)</sub>
      </td>
      <td>
        <img src="static/images/cart.jpg" alt="سبد خرید" width="140" height="100" style="border-radius: 10px; object-fit: cover;">
        <br />
        <strong>سبد خرید</strong><br />
        <sub>(اضافه/حذف کالا)</sub>
      </td>
      <td>
        <img src="static/images/order.png" alt="ثبت سفارش" width="140" height="100" style="border-radius: 10px; object-fit: cover;">
        <br />
        <strong>ثبت سفارش</strong><br />
        <sub>(نهایی‌سازی خرید)</sub>
      </td>
      <td>
        <img src="static/images/products.jpg" alt="محصولات" width="140" height="100" style="border-radius: 10px; object-fit: cover;">
        <br />
        <strong>محصولات و دسته‌بندی</strong><br />
        <sub>(نمایش و فیلتر)</sub>
      </td>
    </tr>
    <tr align="center">
      <td colspan="4">
        <strong>🔐 ثبت‌نام و احراز هویت کاربران + 💳 پرداخت شبیه‌سازی‌شده</strong>
      </td>
    </tr>
    <tr align="center">
      <td colspan="4">
        <strong>✨ API کامل با DRF (RESTful)</strong>
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
