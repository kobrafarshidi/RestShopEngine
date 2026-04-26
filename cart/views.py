from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Cart, CartItem
from Products.models import Products
from .cart_session import SessionCart
from orders.models import Order, OrderItem


def cart_view(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        items = cart.items.all()
        total = sum(item.product.price * item.quantity for item in items)
        cart_items = [
            {
                'id': item.id,
                'product': item.product,
                'quantity': item.quantity,
                'total': item.product.price * item.quantity,
                'is_authenticated': True
            }
            for item in items
        ]
    else:
        session_cart = SessionCart(request)
        items_data = session_cart.get_items()
        cart_items = []
        for item in items_data:
            cart_items.append({
                'id': item['product'].id,
                'product': item['product'],
                'quantity': item['quantity'],
                'total': item['total'],
                'is_authenticated': False
            })
        total = session_cart.get_total_price()

    return render(request, 'cart/cart.html', {
        'items': cart_items,
        'total': total,
        'is_authenticated': request.user.is_authenticated
    })


def add_to_cart(request, product_id):
    product = get_object_or_404(Products, id=product_id)

    if product.stock <= 0:
        messages.error(request, "موجودی این محصول تمام شده")
        return redirect('products:product_detail', pk=product.id)

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            cart_item.quantity += 1
        if cart_item.quantity > product.stock:
            messages.error(request, "بیشتر از موجودی نمی‌توانید خرید کنید")
            return redirect('cart:cart_view')
        cart_item.save()
    else:
        session_cart = SessionCart(request)
        session_cart.add(product_id)

    messages.success(request, f"{product.name} به سبد اضافه شد")
    return redirect('cart:cart_view')


def remove_from_cart(request, item_id):
    if request.user.is_authenticated:
        item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
        item.delete()
    else:
        session_cart = SessionCart(request)
        session_cart.remove(item_id)

    messages.success(request, "محصول حذف شد")
    return redirect('cart:cart_view')


@login_required  # فقط یک بار
def checkout(request):
    cart = Cart.objects.get(user=request.user)

    if not cart.items.exists():
        messages.error(request, "سبد خرید خالی است")
        return redirect('cart:cart_view')

    items = [
        {
            'product': item.product,
            'quantity': item.quantity,
            'total': item.product.price * item.quantity
        }
        for item in cart.items.all()
    ]
    total = sum(item['total'] for item in items)

    if request.method == "POST":
        address = request.POST.get("address")
        phone = request.POST.get("phone")

        order = Order.objects.create(
            user=request.user,
            total_price=total,
            address=address,
            phone=phone
        )

        for item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )
            item.product.stock -= item.quantity
            item.product.save()

        cart.items.all().delete()
        messages.success(request, "سفارش شما با موفقیت ثبت شد")
        return redirect('profile_page')

    return render(request, 'cart/checkout.html', {
        'items': items,
        'total': total
    })


def merge_session_cart_to_db(request):
    if not request.user.is_authenticated:
        return

    session_cart = SessionCart(request)

    if len(session_cart) == 0:
        return

    cart, created = Cart.objects.get_or_create(user=request.user)

    for item in session_cart.get_items():
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=item['product']
        )
        if not created:
            cart_item.quantity += item['quantity']
        else:
            cart_item.quantity = item['quantity']
        cart_item.save()

    session_cart.clear()