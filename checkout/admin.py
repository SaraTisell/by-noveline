from django.contrib import admin
from .models import Order, OrderLineItem

class OrderLineItemAdminInLine(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInLine,)
    
    readonly_fields = ('order_number', 'order_date',
                       'sub_total', 'tax',
                       'shipping_cost', 'grand_total',)
    
    fields = ('order_number', 'user_profile', 'order_date', 'full_name',
              'email', 'phone_number', 'country',
              'town_or_city', 'zip_code', 'street_address1',
              'street_address2', 'county', 'sub_total',
              'tax', 'shipping_cost', 'grand_total',)

    list_display = ('order_number', 'order_date', 'full_name',
                    'sub_total', 'tax', 'shipping_cost',
                    'grand_total',)

    ordering = ('-order_date',)

admin.site.register(Order, OrderAdmin)
