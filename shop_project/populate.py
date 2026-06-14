"""
Скрипт для заполнения базы данных товарами SALMO Shop.
Запуск: python manage.py shell < populate.py
Или:    exec(open('populate.py').read())
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from shop.models import Manufacturer, Category, Product

# --- Производители ---
manufacturers_data = [
    {'name': 'SALMO', 'country': 'Латвия', 'description': 'Ведущий европейский производитель рыболовных снастей'},
    {'name': 'Lucky John', 'country': 'Латвия', 'description': 'Приманки и снасти для хищной рыбы'},
    {'name': 'Daiwa', 'country': 'Япония', 'description': 'Премиальные рыболовные катушки и удилища'},
    {'name': 'Shimano', 'country': 'Япония', 'description': 'Мировой лидер в производстве рыболовного оборудования'},
    {'name': 'Rapala', 'country': 'Финляндия', 'description': 'Легендарные воблеры и приманки'},
]

manufacturers = {}
for data in manufacturers_data:
    obj, created = Manufacturer.objects.get_or_create(name=data['name'], defaults=data)
    manufacturers[data['name']] = obj
    status = 'создан' if created else 'уже есть'
    print(f'  Производитель: {obj.name} — {status}')

# --- Категории ---
categories_data = [
    {'name': 'Удилища', 'description': 'Спиннинги, фидеры, поплавочные удочки'},
    {'name': 'Катушки', 'description': 'Безынерционные и мультипликаторные катушки'},
    {'name': 'Приманки', 'description': 'Воблеры, блёсны, силиконовые приманки'},
    {'name': 'Лески и шнуры', 'description': 'Монофильные лески, плетёные шнуры, флюорокарбон'},
    {'name': 'Крючки и оснастка', 'description': 'Крючки, грузила, поплавки, вертлюжки'},
    {'name': 'Аксессуары', 'description': 'Сумки, ящики, подставки, инструменты'},
]

categories = {}
for data in categories_data:
    obj, created = Category.objects.get_or_create(name=data['name'], defaults=data)
    categories[data['name']] = obj
    status = 'создан' if created else 'уже есть'
    print(f'  Категория: {obj.name} — {status}')

# --- Товары ---
products_data = [
    # Удилища
    {'name': 'Спиннинг SALMO Sniper 2.4м', 'description': 'Универсальный спиннинг для ловли хищника. Карбоновый бланк, тест 5-25г, быстрый строй. Идеален для джига и воблеров.', 'price': 89.90, 'stock_quantity': 15, 'category': 'Удилища', 'manufacturer': 'SALMO'},
    {'name': 'Фидер SALMO Diamond 3.6м', 'description': 'Фидерное удилище среднего класса. Тест до 120г, 3 сменные вершинки. Отлично подходит для ловли на реке и озере.', 'price': 125.00, 'stock_quantity': 8, 'category': 'Удилища', 'manufacturer': 'SALMO'},
    {'name': 'Спиннинг Daiwa Ninja X 2.7м', 'description': 'Премиальный спиннинг от Daiwa. Высокомодульный карбон, Fuji кольца, тест 7-28г.', 'price': 245.00, 'stock_quantity': 5, 'category': 'Удилища', 'manufacturer': 'Daiwa'},
    {'name': 'Поплавочная удочка Shimano Catana 4м', 'description': 'Телескопическое удилище для поплавочной ловли. Лёгкое и чувствительное, вес всего 180г.', 'price': 67.50, 'stock_quantity': 20, 'category': 'Удилища', 'manufacturer': 'Shimano'},

    # Катушки
    {'name': 'Катушка Shimano Sedona 2500', 'description': 'Безынерционная катушка с передним фрикционом. 4 подшипника, передаточное число 5.0:1. Плавный ход и надёжность.', 'price': 159.90, 'stock_quantity': 12, 'category': 'Катушки', 'manufacturer': 'Shimano'},
    {'name': 'Катушка Daiwa Crossfire 3000', 'description': 'Надёжная катушка для спиннинговой ловли. Система Digigear, алюминиевая шпуля, вес 270г.', 'price': 135.00, 'stock_quantity': 10, 'category': 'Катушки', 'manufacturer': 'Daiwa'},
    {'name': 'Катушка SALMO Elite 4000', 'description': 'Мощная катушка для фидерной и карповой ловли. Байтраннер, 6 подшипников, шпуля из нержавеющей стали.', 'price': 78.00, 'stock_quantity': 18, 'category': 'Катушки', 'manufacturer': 'SALMO'},

    # Приманки
    {'name': 'Воблер Rapala Original 11см', 'description': 'Классический плавающий воблер. Рабочая глубина 1.2-1.8м. Проверенная десятилетиями игра.', 'price': 24.90, 'stock_quantity': 50, 'category': 'Приманки', 'manufacturer': 'Rapala'},
    {'name': 'Воблер Lucky John Pro Vibe 7см', 'description': 'Тонущий воблер для ловли судака и окуня. Активная игра на равномерной проводке и стоп-энд-гоу.', 'price': 18.50, 'stock_quantity': 40, 'category': 'Приманки', 'manufacturer': 'Lucky John'},
    {'name': 'Блесна SALMO Hornet 5г', 'description': 'Вращающаяся блесна с серебристым лепестком. Стабильная работа на медленной проводке.', 'price': 8.90, 'stock_quantity': 100, 'category': 'Приманки', 'manufacturer': 'SALMO'},
    {'name': 'Силиконовая приманка Lucky John Tioga 8см', 'description': 'Съедобный силикон с аттрактантом. Реалистичная игра хвоста, 10 шт в упаковке.', 'price': 12.50, 'stock_quantity': 60, 'category': 'Приманки', 'manufacturer': 'Lucky John'},
    {'name': 'Набор блёсен SALMO Master Kit (10 шт)', 'description': 'Набор из 10 вращающихся и колеблющихся блёсен разного веса. В удобном кейсе.', 'price': 35.00, 'stock_quantity': 25, 'category': 'Приманки', 'manufacturer': 'SALMO'},

    # Лески и шнуры
    {'name': 'Плетёный шнур SALMO Braid 150м 0.12мм', 'description': 'Прочный плетёный шнур из 4 нитей. Разрывная нагрузка 8кг, минимальная память.', 'price': 22.00, 'stock_quantity': 30, 'category': 'Лески и шнуры', 'manufacturer': 'SALMO'},
    {'name': 'Леска Shimano Technium 300м 0.25мм', 'description': 'Монофильная леска с низкой памятью. Устойчива к УФ-излучению, прозрачная.', 'price': 15.90, 'stock_quantity': 45, 'category': 'Лески и шнуры', 'manufacturer': 'Shimano'},

    # Крючки и оснастка
    {'name': 'Крючки SALMO Specialist №6 (20 шт)', 'description': 'Острые кованые крючки с химической заточкой. С бородкой, чёрные никелированные.', 'price': 4.50, 'stock_quantity': 200, 'category': 'Крючки и оснастка', 'manufacturer': 'SALMO'},
    {'name': 'Набор грузил Daiwa 50г (10 шт)', 'description': 'Набор свинцовых грузил разного веса от 10 до 50г. Для фидерной и донной ловли.', 'price': 9.90, 'stock_quantity': 35, 'category': 'Крючки и оснастка', 'manufacturer': 'Daiwa'},

    # Аксессуары
    {'name': 'Подсачек SALMO складной 60см', 'description': 'Складной подсачек с телескопической ручкой. Мягкая сетка, не травмирует рыбу.', 'price': 28.00, 'stock_quantity': 22, 'category': 'Аксессуары', 'manufacturer': 'SALMO'},
    {'name': 'Сумка-холодильник Lucky John 25л', 'description': 'Термосумка для сохранения улова. Водонепроницаемая подкладка, регулируемый ремень.', 'price': 42.00, 'stock_quantity': 14, 'category': 'Аксессуары', 'manufacturer': 'Lucky John'},
    {'name': 'Эхолот Lucky John FF-718', 'description': 'Портативный эхолот с цветным дисплеем. Глубина сканирования до 50м, беспроводной датчик.', 'price': 189.00, 'stock_quantity': 0, 'category': 'Аксессуары', 'manufacturer': 'Lucky John'},
]

print(f'\nДобавляем {len(products_data)} товаров...')
for data in products_data:
    cat = categories[data.pop('category')]
    mfr = manufacturers[data.pop('manufacturer')]
    obj, created = Product.objects.get_or_create(
        name=data['name'],
        defaults={
            'description': data['description'],
            'price': data['price'],
            'stock_quantity': data['stock_quantity'],
            'category': cat,
            'manufacturer': mfr,
        }
    )
    status = 'создан' if created else 'уже есть'
    stock = 'НЕТ В НАЛИЧИИ' if data['stock_quantity'] == 0 else f"{data['stock_quantity']} шт."
    print(f'  [{status}] {obj.name} — {obj.price} руб. ({stock})')

total = Product.objects.count()
print(f'\n✅ Готово! Всего товаров в базе: {total}')
