FROM python:3.12-slim

# جلوگیری از تولید فایل‌های .pyc و فعال شدن خروجی رنگی
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# نصب وابستگی‌های سیستمی برای psycopg2 و pillow
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# پوشه پروژه داخل کانتینر
WORKDIR /app

# کپی فایل‌های requirements
COPY requirements.txt .

# نصب پکیج‌ها
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# کپی کل پروژه داخل کانتینر
COPY . .

# جمع‌آوری فایل‌های static (برا admin و frontend)
RUN python manage.py collectstatic --noinput

# تنظیم پورت 8000 (پورت پیش‌فرض Django)
EXPOSE 8000

# اجرای migrationها و اجرای برنامه با gunicorn
CMD sh -c "python manage.py migrate && gunicorn core.wsgi:application --bind 0.0.0.0:8000"
