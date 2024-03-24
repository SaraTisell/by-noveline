from decimal import Decimal
from django.shortcuts import get_object_or_404
from products.models import Product

def cart_contents(request):

    cart_items = []
    product_count = 0
    subtotal = 0
    tax_rate = Decimal('0.10')
    shipping_cost = 9
    cart = request.session.get('cart', {})

    for item_id, item_data in cart.items():
        if isinstance(item_data, dict):
            quantity = item_data.get('quantity', 1)
            size = item_data.get('size')
            size2 = item_data.get('size2')
            product = get_object_or_404(Product, pk=item_id)
            subtotal += quantity * product.price
            product_count += quantity
            cart_items.append({
                'item_id': item_id,
                'quantity': quantity,
                'product': product,
                'size': size,
                'size2': size2,
            })   

    tax = subtotal * tax_rate
    grand_total = shipping_cost + subtotal + tax



    context = {
        'cart_items': cart_items,
        'product_count': product_count,
        'subtotal': subtotal,
        'tax': tax,
        'shipping_cost': shipping_cost,
        'grand_total': grand_total,
    }

    return context