from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib import admin
from .models import Order, OrderItem, Customer
from products.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'description')
    search_fields = ('name', 'category__name')
    list_filter = ('category',)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ['total']
    list_display = ('id', 'customer', 'date', 'status', 'total')
    list_filter = ('status', 'date')
    search_fields = ('customer__name', 'id')
    inlines = [OrderItemInline]


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address')
    search_fields = ('name', 'email')
    list_filter = ('name',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Customer, CustomerAdmin)


@receiver(post_save, sender=Order)
def update_order_total(sender, instance, created, **kwargs):
    if created:
        instance.total = instance.calculate_total()
        instance.save()

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'quantity', 'price', 'total_price')
    search_fields = ('order__id', 'product__name')
    list_filter = ('order__date',)

    def total_price(self, obj):
        return obj.total_price()
    total_price.short_description = 'Total Price'
