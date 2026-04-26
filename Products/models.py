from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام دسته‌بندی')
    slug = models.SlugField(unique=True, verbose_name='اسلاگ')

    class Meta:
        verbose_name = 'دسته‌بندی'
        verbose_name_plural = 'دسته‌بندی‌ها'

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام محصول')
    description = models.TextField(verbose_name='توضیحات')  # تغییر از info به description
    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='قیمت')
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name='تصویر')
    stock = models.PositiveIntegerField(default=0, verbose_name='موجودی')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='products', verbose_name='دسته‌بندی')
    color = models.CharField(max_length=50, blank=True, verbose_name='رنگ')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return self.name


class ProductLike(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='product_likes')
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')
        verbose_name = 'لایک محصول'
        verbose_name_plural = 'لایک‌های محصولات'

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"
