from rest_framework import serializers
from .models import Manufacturer, Category, Product, Cart, CartItem


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    manufacturer_name = serializers.CharField(source='manufacturer.name', read_only=True)

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'description', 'photo',
            'price', 'stock_quantity',
            'category', 'category_name',
            'manufacturer', 'manufacturer_name',
        ]


class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    item_cost = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = CartItem
        fields = ['id', 'cart', 'product', 'product_name', 'quantity', 'item_cost']


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(source='cartitem_set', many=True, read_only=True)
    total_cost = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'username', 'created_at', 'total_cost', 'items']
