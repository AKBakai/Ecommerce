from django.contrib import admin
from order.models import Order, OrderItem

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'full_name',
        'address1',
        'address2',
        'city',
        'phone',
        'created',
        'updated',
        'total_paid',
        'order_key',
        'billing_status'
    )

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        'price',
        'quantity'
    )
