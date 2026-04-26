from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Products import views as product_views

urlpatterns = [
    path('', product_views.home, name='home'),
    path('admin/', admin.site.urls),

    # Products
    path('products/', product_views.product_list, name='product_list'),
    path('products/<int:pk>/', product_views.product_detail, name='product_detail'),
    path('categories/', product_views.category_list, name='category_list'),
    path('category/<slug:slug>/', product_views.category_products, name='category_products'),

    # Accounts
    path('accounts/', include('accounts.urls')),

    # Cart
    path('cart/', include('cart.urls')),

    # API endpoints
    path('api/products/', include('Products.urls')),
    path('api/accounts/', include('accounts.urls')),
    path('api/cart/', include('cart.urls')),
    path('api/orders/', include('orders.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
