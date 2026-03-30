from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# --- ЗАДАНИЕ 1 ---

class Manufacturer(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    country = models.CharField(max_length=100, verbose_name="Страна")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория товара"
        verbose_name_plural = "Категории товаров"


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    photo = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name="Фото товара")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    stock_quantity = models.IntegerField(verbose_name="Количество на складе")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, verbose_name="Производитель")

    def clean(self):
        # Валидация: цена и количество не могут быть отрицательными
        if self.price is not None and self.price < 0:
            raise ValidationError({'price': 'Цена не может быть отрицательной.'})
        if self.stock_quantity is not None and self.stock_quantity < 0:
            raise ValidationError({'stock_quantity': 'Количество на складе не может быть отрицательным.'})

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


# --- ЗАДАНИЕ 2 ---

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def total_cost(self):
        # Вычисляет сумму стоимости всех элементов корзины
        return sum(item.item_cost() for item in self.cartitem_set.all())

    def __str__(self):
        return f"Корзина пользователя {self.user.username}"

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name="Корзина")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар")
    quantity = models.PositiveIntegerField(verbose_name="Количество")

    def item_cost(self):
        # Возвращает товар.цена * количество
        return self.product.price * self.quantity

    def clean(self):
        # Валидация: количество не должно превышать остаток на складе
        if self.quantity is not None and self.product is not None:
            if self.quantity > self.product.stock_quantity:
                raise ValidationError({'quantity': f'Доступно только {self.product.stock_quantity} шт. товара.'})

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product.name} ({self.quantity} шт.)"

    class Meta:
        verbose_name = "Элемент корзины"
        verbose_name_plural = "Элементы корзины"


# --- ЗАДАНИЕ 3: Модель заказа ---

class Order(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новый'),
        ('processing', 'В обработке'),
        ('shipped', 'Отправлен'),
        ('delivered', 'Доставлен'),
        ('cancelled', 'Отменён'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new', verbose_name="Статус")
    
    # Данные доставки
    name = models.CharField(max_length=200, verbose_name="Имя получателя")
    phone = models.CharField(max_length=50, verbose_name="Телефон")
    address = models.TextField(verbose_name="Адрес доставки")
    payment_method = models.CharField(max_length=20, verbose_name="Способ оплаты")
    
    # Итоговая сумма
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Общая сумма")
    
    # Email для отправки чека
    email = models.EmailField(verbose_name="Email для уведомлений", blank=True, null=True)

    def __str__(self):
        return f"Заказ №{self.id} от {self.user.username}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        ordering = ['-created_at']


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', verbose_name="Заказ")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар")
    quantity = models.PositiveIntegerField(verbose_name="Количество")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена на момент заказа")

    def item_cost(self):
        return self.price * self.quantity

    def __str__(self):
        return f"{self.product.name} ({self.quantity} шт.)"

    class Meta:
        verbose_name = "Элемент заказа"
        verbose_name_plural = "Элементы заказа"
