from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Manufacturer, Category, Product, Cart, CartItem, Order, OrderItem, Profile


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


# --- Profile & User ---

class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)
    role_display = serializers.CharField(read_only=True)
    favorite_category_name = serializers.CharField(source='favorite_category.name', read_only=True, default='')

    class Meta:
        model = Profile
        fields = [
            'username', 'email', 'role', 'role_display',
            'full_name', 'phone', 'address',
            'city', 'postal_code', 'favorite_category', 'favorite_category_name',
            'avatar',
        ]
        read_only_fields = ['role']


# --- Orders ---

class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    item_cost = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'product_name', 'quantity', 'price', 'item_cost']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Order
        fields = [
            'id', 'user', 'username', 'created_at', 'status', 'status_display',
            'name', 'phone', 'address', 'payment_method',
            'total_amount', 'email', 'items',
        ]
        read_only_fields = ['user', 'created_at', 'total_amount']
