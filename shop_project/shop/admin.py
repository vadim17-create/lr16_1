from django.contrib import admin
from .models import Manufacturer, Category, Product, Cart, CartItem, Order, OrderItem

admin.site.register(Manufacturer)
admin.site.register(Category)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock_quantity', 'category', 'manufacturer')
    list_filter = ('category', 'manufacturer')
    search_fields = ('name',)

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'total_cost_display')

    def total_cost_display(self, obj):
        return f"{obj.total_cost()} руб."
    total_cost_display.short_description = 'Общая стоимость'

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity', 'item_cost_display')

    def item_cost_display(self, obj):
        return f"{obj.item_cost()} руб."
    item_cost_display.short_description = 'Стоимость'

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at', 'status', 'total_amount', 'name', 'phone')
    list_filter = ('status', 'payment_method', 'created_at')
    search_fields = ('user__username', 'name', 'phone')
    readonly_fields = ('created_at',)

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price', 'item_cost_display')

    def item_cost_display(self, obj):
        return f"{obj.item_cost()} руб."
    item_cost_display.short_description = 'Стоимость'
