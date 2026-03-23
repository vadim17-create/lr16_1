from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from decimal import Decimal
from .models import Product, Category


def cyrillic_icontains(field, query):
    return (
        Q(**{f'{field}__contains': query}) |
        Q(**{f'{field}__contains': query.lower()}) |
        Q(**{f'{field}__contains': query.capitalize()}) |
        Q(**{f'{field}__contains': query.upper()})
    )


def _get_cart(request):
    return request.session.get('cart', {})


def _save_cart(request, cart):
    request.session['cart'] = cart
    request.session.modified = True


def _cart_count(request):
    return sum(_get_cart(request).values())


def home(request):
    return render(request, 'home.html', {'cart_count': _cart_count(request)})


def about(request):
    table_rows = [
        ('Удочка телескопическая', 'Лёгкая, 3 м', '35 руб.'),
        ('Катушка рыболовная', 'С фрикционом', '50 руб.'),
        ('Леска 0.25 мм', '100 м, монофильная', '12 руб.'),
        ('Поплавок 5 г', 'Плавающий', '3 руб.'),
        ('Крючки №6', 'Набор 50 шт', '7 руб.'),
        ('Силиконовые приманки', 'Набор 10 шт', '15 руб.'),
        ('Блесна вращающаяся', '7 г, цвет серебро', '8 руб.'),
        ('Сачок складной', '50 см, сетка', '25 руб.'),
        ('Эхолот рыбопоисковый', 'С ЖК-дисплеем', '120 руб.'),
        ('Воблер плавающий', '8 см, цвет рыба', '20 руб.'),
    ]
    return render(request, 'about.html', {'table_rows': table_rows, 'cart_count': _cart_count(request)})


def author(request):
    return render(request, 'author.html', {'cart_count': _cart_count(request)})


def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    search_query = request.GET.get('search', '').strip()
    if search_query:
        products = products.filter(cyrillic_icontains('name', search_query))

    category_id = request.GET.get('category', '')
    if category_id:
        products = products.filter(category_id=category_id)

    sort_by = request.GET.get('sort', '')
    if sort_by == 'cheap':
        products = products.order_by('price')
    elif sort_by == 'expensive':
        products = products.order_by('-price')

    return render(request, 'catalog.html', {
        'products': products,
        'categories': categories,
        'search_query': search_query,
        'category_id': category_id,
        'sort_by': sort_by,
        'total': products.count(),
        'cart_count': _cart_count(request),
    })


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {
        'product': product,
        'cart_count': _cart_count(request),
    })


# ─── КОРЗИНА ────────────────────────────────────────────────────────────────

@csrf_exempt
def cart_add(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart = _get_cart(request)
    key = str(pk)
    qty = int(request.POST.get('quantity', 1))
    cart[key] = min(cart.get(key, 0) + qty, product.stock_quantity)
    _save_cart(request, cart)
    return redirect(request.META.get('HTTP_REFERER', '/catalog/'))


@csrf_exempt
def cart_remove(request, pk):
    cart = _get_cart(request)
    cart.pop(str(pk), None)
    _save_cart(request, cart)
    return redirect('/cart/')


@csrf_exempt
def cart_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart = _get_cart(request)
    qty = int(request.POST.get('quantity', 1))
    if qty <= 0:
        cart.pop(str(pk), None)
    else:
        cart[str(pk)] = min(qty, product.stock_quantity)
    _save_cart(request, cart)
    return redirect('/cart/')


def cart_view(request):
    cart = _get_cart(request)
    items, total = _build_cart_items(cart)
    return render(request, 'cart.html', {
        'items': items,
        'total': total,
        'cart_count': _cart_count(request),
    })


def cart_clear(request):
    _save_cart(request, {})
    return redirect('/cart/')


def _build_cart_items(cart):
    items = []
    total = Decimal('0')
    for pid, qty in cart.items():
        try:
            product = Product.objects.get(pk=int(pid))
            subtotal = product.price * qty
            total += subtotal
            items.append({'product': product, 'qty': qty, 'subtotal': subtotal})
        except Product.DoesNotExist:
            pass
    return items, total


# ─── ОФОРМЛЕНИЕ ЗАКАЗА ──────────────────────────────────────────────────────

def checkout(request):
    cart = _get_cart(request)
    if not cart:
        return redirect('/cart/')

    items, total = _build_cart_items(cart)
    error = ''
    form_data = {'name': '', 'phone': '', 'address': ''}

    if request.method == 'POST':
        form_data = {
            'name': request.POST.get('name', '').strip(),
            'phone': request.POST.get('phone', '').strip(),
            'address': request.POST.get('address', '').strip(),
        }
        if not all(form_data.values()):
            error = '⚠️ Заполните все поля.'
        else:
            _save_cart(request, {})
            return redirect('/order-success/')

    return render(request, 'checkout.html', {
        'items': items,
        'total': total,
        'error': error,
        'form_data': form_data,
        'cart_count': _cart_count(request),
    })


def order_success(request):
    return render(request, 'order_success.html', {'cart_count': 0})
