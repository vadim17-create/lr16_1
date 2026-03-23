from django.contrib import admin
from .models import Manufacturer, Category, Product, Cart, CartItem

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
        return obj.total_cost()
    total_cost_display.short_description = 'Общая стоимость'

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity', 'item_cost_display')
    
    def item_cost_display(self, obj):
        return obj.item_cost()
    item_cost_display.short_description = 'Стоимость'
