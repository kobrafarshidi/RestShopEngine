from .models import Cart
from .cart_session import SessionCart


def cart_counter(request):
    count = 0

    if request.user.is_authenticated:
        try:
            cart = Cart.objects.get(user=request.user)
            count = sum(item.quantity for item in cart.items.all())
        except Cart.DoesNotExist:
            count = 0
    else:
        session_cart = SessionCart(request)
        count = len(session_cart)

    return {'cart_count': count}
