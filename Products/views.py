from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Products, Category
from .serializers import ProductsSerializer


class ProductsView(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['stock']
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'created_at']


def home(request):
    return render(request, 'home.html')


def product_list(request):
    """لیست تمام محصولات"""
    sort_by = request.GET.get('sort', 'created_at')
    if sort_by == 'price_asc':
        products = Products.objects.filter(stock__gt=0).order_by('price')
    elif sort_by == 'price_desc':
        products = Products.objects.filter(stock__gt=0).order_by('-price')
    else:
        products = Products.objects.filter(stock__gt=0).order_by('-created_at')

    return render(request, 'products/product_list.html', {
        'products': products,
        'sort_by': sort_by
    })


def product_detail(request, pk):
    """جزئیات یک محصول خاص"""
    product = get_object_or_404(Products, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})


def category_list(request):
    """لیست دسته‌بندی‌ها"""
    categories = Category.objects.all()
    return render(request, 'products/category_list.html', {'categories': categories})


def category_products(request, slug):
    """محصولات یک دسته‌بندی خاص"""
    category = get_object_or_404(Category, slug=slug)
    products = Products.objects.filter(category=category, stock__gt=0)
    return render(request, 'products/category_products.html', {
        'category': category,
        'products': products
    })
