from django.shortcuts import render
from products.models import Product


def index(request):
    """ View to return index as home page
        Include latest products ordered by id
    """
    latest_products = Product.objects.order_by('-id')[:4]

    return render(
        request, 'home/index.html', {'latest_products': latest_products})


def privacy_policy(request):
    """ View to render privacy policy """
    return render(request, 'home/privacy_policy.html')
