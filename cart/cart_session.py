from Products.models import Products


class SessionCart:

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def add(self, product_id, quantity=1):
        product_id = str(product_id)
        if product_id in self.cart:
            self.cart[product_id]['quantity'] += quantity
        else:
            self.cart[product_id] = {'quantity': quantity}
        self.save()

    def remove(self, product_id):
        product_id = str(product_id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def get_items(self):
        product_ids = self.cart.keys()
        products = Products.objects.filter(id__in=product_ids)
        items = []

        for product in products:
            item = {
                'product': product,
                'quantity': self.cart[str(product.id)]['quantity'],
                'total': product.price * self.cart[str(product.id)]['quantity']
            }
            items.append(item)
        return items

    def get_total_price(self):
        return sum(item['total'] for item in self.get_items())

    def clear(self):
        del self.session['cart']
        self.save()

    def save(self):
        self.session.modified = True

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
