from .models import WishList, WishListItem


def wishlist_contents(request):
    wishlist = None
    wishlist_items = None
    if request.user.is_authenticated:
        wishlist, created = WishList.objects.get_or_create(user=request.user)
        wishlist_items = wishlist.products.all()
    return {
        'wishlist': wishlist,
        'wishlist_items': wishlist_items,
    }