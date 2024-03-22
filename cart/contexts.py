
def cart_contents(request):

    cart_items = []
    product_count = 0
    subtotal = 0
    tax_rate = 0.10
    shipping_cost = 9

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