from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def home(request):
    return HttpResponse(
        """
        <h1>Главная страница магазина</h1>
        <p>Добро пожаловать на мини-сайт магазина!</p>
        <ul>
            <li><a href='/about/'>О магазине</a></li>
            <li><a href='/author/'>Об авторе</a></li>
            <li><b><a href='/catalog/'>Каталог товаров </a></b></li>
        </ul>
        """
    )
def about(request):
    return HttpResponse(
        """
        <h1>О магазине</h1>
        <br><a href='https://www.salmo.by/?srsltid=AfmBOorK6ctFK3KR0yPAQLk_-mb3ln30L5-9vyCb-oySW4rHkl-HwbVD'>SALMO</a>
        <p>Создание и базовая настройка приложений Django. Рыболовные товары от salmo</p>
        <table border='1' cellpadding='5'>
            <tr>
                <th>Товар</th>
                <th>Описание</th>
                <th>Цена</th>
            </tr>
           <tr>
    <td>Удочка телескопическая</td>
    <td>Лёгкая, 3 м</td>
    <td>35 рублей</td>
</tr>
<tr>
    <td>Катушка рыболовная</td>
    <td>С фрикционом</td>
    <td>50 рублей</td>
</tr>
<tr>
    <td>Леска 0.25 мм</td>
    <td>100 м, монофильная</td>
    <td>12 рублей</td>
</tr>
<tr>
    <td>Поплавок 5 г</td>
    <td>Плавающий</td>
    <td>3 рублей</td>
</tr>
<tr>
    <td>Крючки №6</td>
    <td>Набор 50 шт</td>
    <td>7 рублей</td>
</tr>
<tr>
    <td>Силиконовые приманки</td>
    <td>Набор 10 шт</td>
    <td>15 рублей</td>
</tr>
<tr>
    <td>Блесна вращающаяся</td>
    <td>7 г, цвет серебро</td>
    <td>8 рублей</td>
</tr>
<tr>
    <td>Мотовило для лески</td>
    <td>Пластиковое</td>
    <td>4 рублей</td>
</tr>
<tr>
    <td>Сачок складной</td>
    <td>50 см, сетка</td>
    <td>25 рублей</td>
</tr>
<tr>
    <td>Эхолот рыбопоисковый</td>
    <td>С ЖК-дисплеем</td>
    <td>120 рублей</td>
</tr>
<tr>
    <td>Короповый крючок №4</td>
    <td>Набор 25 шт</td>
    <td>10 рублей</td>
</tr>
<tr>
    <td>Кормушка для рыбы</td>
    <td>Металлическая, 40 г</td>
    <td>6 рублей</td>
</tr>
<tr>
    <td>Воблер плавающий</td>
    <td>8 см, цвет рыба</td>
    <td>20 рублей</td>
</tr>
<tr>
    <td>Поплавки пенопластовые</td>
    <td>Набор 5 шт</td>
    <td>5 рублей</td>
</tr>
<tr>
    <td>Нож для рыбалки</td>
    <td>Складной, нержавейка</td>
    <td>18 рублей</td>
</tr>
<tr>
    <td>Щипцы для крючков</td>
    <td>Металлические</td>
    <td>12 рублей</td>
</tr>
<tr>
    <td>Подсачек для карпа</td>
    <td>Сетка 60 см</td>
    <td>30 рублей</td>
</tr>
<tr>
    <td>Сумка для снастей</td>
    <td>Водонепроницаемая</td>
    <td>40 рублей</td>
</tr>
<tr>
    <td>Весы электронные</td>
    <td>До 50 кг</td>
    <td>55 рублей</td>
</tr>
<tr>
    <td>Сигнализатор поклёвки</td>
    <td>Светозвуковой</td>
    <td>22 рублей</td>
</tr>
<tr>
    <td>Леска плетёная</td>
    <td>0.20 мм, 150 м</td>
    <td>18 рублей</td>
</tr>
<tr>
    <td>Резина для приманок</td>
    <td>Набор 20 шт</td>
    <td>7 рублей</td>
</tr>
<tr>
    <td>Плавающий поплавок</td>
    <td>10 г</td>
    <td>4 рублей</td>
</tr>
<tr>
    <td>Набор грузил</td>
    <td>От 5 до 30 г</td>
    <td>9 рублей</td>
</tr>
<tr>
    <td>Кепка рыболовная</td>
    <td>С козырьком</td>
    <td>15 рублей</td>
</tr>
<tr>
    <td>Очки поляризационные</td>
    <td>Защита от бликов</td>
    <td>45 рублей</td>
</tr>
<tr>
    <td>Палатка рыболовная</td>
    <td>1-местная, водонепроницаемая</td>
    <td>80 рублей</td>
</tr>
<tr>
    <td>Сидение складное</td>
    <td>Лёгкое, алюминиевое</td>
    <td>28 рублей</td>
</tr>
<tr>
    <td>Термос 1 л</td>
    <td>Нержавейка</td>
    <td>35 рублей</td>
</tr>
<tr>
    <td>Перчатки рыболовные</td>
    <td>Неопреновые</td>
    <td>20 рублей</td>
</tr>
<tr>
    <td>Фонарь налобный</td>
    <td>LED, 3 режима</td>
    <td>17 рублей</td>
</tr>
<tr>
    <td>Сумка-холодильник</td>
    <td>20 л</td>
    <td>50 рублей</td>
</tr>
<tr>
    <td>Кресло рыболовное</td>
    <td>Складное, с подлокотниками</td>
    <td>60 рублей</td>
</tr>
<tr>
    <td>Лопатка для прикормки</td>
    <td>Деревянная</td>
    <td>5 рублей</td>
</tr>
<tr>
    <td>Ведро складное</td>
    <td>10 л, силикон</td>
    <td>12 рублей</td>
</tr>
<tr>
    <td>Сетка для рыбы</td>
    <td>Длина 1 м</td>
    <td>18 рублей</td>
</tr>
<tr>
    <td>Сумка для живца</td>
    <td>С аквариумной сеткой</td>
    <td>25 рублей</td>
</tr>
<tr>
    <td>Термоковрик для рыбалки</td>
    <td>С водонепроницаемой подкладкой</td>
    <td>22 рублей</td>
</tr>
<tr>
    <td>Палочка для кормушки</td>
    <td>Металлическая, 50 см</td>
    <td>6 рублей</td>
</tr>
<tr>
    <td>Эхолот для телефона</td>
    <td>Wi-Fi подключение</td>
    <td>90 рублей</td>
</tr>
<tr>
    <td>Грузила свинцовые</td>
    <td>Набор 10 шт</td>
    <td>10 рублей</td>
</tr>
<tr>
    <td>Сачок для раков</td>
    <td>Сетка 70 см</td>
    <td>33 рублей</td>
</tr>
<tr>
    <td>Палатка зимняя</td>
    <td>Для рыбалки на льду</td>
    <td>120 рублей</td>
</tr>
<tr>
    <td>Термокружка</td>
    <td>350 мл, нержавейка</td>
    <td>18 рублей</td>
</tr>
<tr>
    <td>Набор приманок</td>
    <td>Мягкие и твистеры</td>
    <td>30 рублей</td>
</tr>
<tr>
    <td>Коврик для рыбака</td>
    <td>Складной, мягкий</td>
    <td>40 рублей</td>
</tr>
<tr>
    <td>Подставка для удочки</td>
    <td>Металл, 2 шт</td>
    <td>15 рублей</td>
</tr>
<tr>
    <td>Сигнализатор поклёвки</td>
    <td>Беспроводной</td>
    <td>35 рублей</td>
</tr>
<tr>
    <td>Поясная сумка</td>
    <td>Для снастей</td>
    <td>20 рублей</td>
</tr>
<tr>
    <td>Фонарь на батарейках</td>
    <td>3 режима свечения</td>
    <td>10 рублей</td>
</tr>
<tr>
    <td>Набор крючков</td>
    <td>Разные размеры, 100 шт</td>
    <td>12 рублей</td>
</tr>
<tr>
    <td>Леска карповая 0.30 мм</td>
    <td>150 м</td>
    <td>20 рублей</td>
</tr>
<tr>
    <td>Набор свистков и сигналов</td>
    <td>Для безопасности на воде</td>
    <td>7 рублей</td>
</tr>
<tr>
    <td>Сумка для спиннингов</td>
    <td>Длинная, для 2 удилищ</td>
    <td>60 рублей</td>
</tr>
        </table>
        <p><a href='/'>На главную</a></p>
        """
    )

def author(request):
    return HttpResponse(
        """
        <h1>Об авторе</h1>
        <p>Лабораторную работу выполнил: Бабич Вадим Александрович</p>
        <p><a href='/'>На главную</a></p>
        """
    )


def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    # 1. Поиск по названию
    search_query = request.GET.get('search', '').strip()
    if search_query:
        products = products.filter(name__icontains=search_query)

    # 2. Фильтрация по категории
    category_id = request.GET.get('category', '')
    if category_id:
        products = products.filter(category_id=category_id)

    # 3. Сортировка по цене
    sort_by = request.GET.get('sort', '')
    if sort_by == 'cheap':
        products = products.order_by('price')
    elif sort_by == 'expensive':
        products = products.order_by('-price')

    # Строим HTML для списка категорий
    category_options = '<option value="">Все категории</option>'
    for cat in categories:
        category_options += f'<option value="{cat.id}">{cat.name}</option>'

    # Строим HTML для карточек товаров
    products_html = ''
    for product in products:
        products_html += f"""
        <div style="border: 1px solid #ccc; padding: 15px; width: 220px; border-radius: 5px;">
            <h4 style="margin: 0 0 10px 0;">{product.name}</h4>
            <p>📂 {product.category.name}</p>
            <p>🏭 {product.manufacturer.name}</p>
            <p style="color: green; font-weight: bold; font-size: 18px;">{product.price} руб.</p>
            <p>📦 Остаток: {product.stock_quantity} шт.</p>
            <a href="/catalog/{product.pk}/">Подробнее →</a>
        </div>
        """

    if not products_html:
        products_html = '<p>❌ Товары по вашему запросу не найдены.</p>'

    total = products.count()

    html = f"""
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>Каталог товаров</title>
    </head>
    <body style="font-family: Arial, sans-serif; padding: 20px;">

        <h1>Каталог товаров</h1>
        <p><a href="/">← На главную</a></p>

        <div style="background-color: #f0f0f0; padding: 15px; margin-bottom: 20px; border-radius: 5px;">
            <h3>Поиск и фильтрация:</h3>
            <form method="get" action="/catalog/">
                <label>🔍 Поиск по названию:</label>
                <input type="text" name="search" value="{search_query}" placeholder="Введите название...">

                <label>📂 Категория:</label>
                <select name="category">
                    {category_options}
                </select>

                <label>↕️ Сортировка:</label>
                <select name="sort">
                    <option value="">Без сортировки</option>
                    <option value="cheap">Сначала дешевые</option>
                    <option value="expensive">Сначала дорогие</option>
                </select>

                <button type="submit">Применить</button>
                <a href="/catalog/"><button type="button">Сбросить</button></a>
            </form>
        </div>

        <h3>Найдено товаров: {total}</h3>
        <div style="display: flex; flex-wrap: wrap; gap: 20px;">
            {products_html}
        </div>

    </body>
    </html>
    """
    return HttpResponse(html)


def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return HttpResponse("<h1>Товар не найден</h1><a href='/catalog/'>Назад</a>")

    html = f"""
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>{product.name}</title>
    </head>
    <body style="font-family: Arial, sans-serif; padding: 20px;">

        <p><a href="/catalog/">← Назад к списку товаров</a></p>

        <h1>{product.name}</h1>

        <div style="margin-top: 20px;">
            <p>📂 <b>Категория:</b> {product.category.name}</p>
            <p>🏭 <b>Производитель:</b> {product.manufacturer.name} ({product.manufacturer.country})</p>
            <p>📝 <b>Описание:</b> {product.description}</p>
            <p style="color: green; font-weight: bold; font-size: 28px;">💰 {product.price} руб.</p>
            <p>📦 <b>Наличие на складе:</b> {product.stock_quantity} шт.</p>
        </div>

    </body>
    </html>
    """
    return HttpResponse(html)