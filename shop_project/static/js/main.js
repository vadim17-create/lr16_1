/* ================================================
   SALMO Shop — main.js
   Взаимодействие с API через JavaScript
   ================================================ */

// ─── CSRF Token ─────────────────────────────────────────────────────────────
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

// ─── Spinner ────────────────────────────────────────────────────────────────
function showSpinner() {
    const overlay = document.getElementById('spinner-overlay');
    if (overlay) overlay.classList.add('active');
}

function hideSpinner() {
    const overlay = document.getElementById('spinner-overlay');
    if (overlay) overlay.classList.remove('active');
}

// ─── Toast Notifications ────────────────────────────────────────────────────
function showToast(message, type = 'success') {
    const container = document.getElementById('toast-container');
    if (!container) return;

    const icons = {
        success: '✅',
        danger: '❌',
        warning: '⚠️',
        info: 'ℹ️'
    };

    const toast = document.createElement('div');
    toast.className = `toast align-items-center text-bg-${type} border-0 show`;
    toast.setAttribute('role', 'alert');
    toast.innerHTML = `
        <div class="d-flex">
            <div class="toast-body">
                ${icons[type] || ''} ${message}
            </div>
            <button type="button" class="btn-close btn-close-white me-2 m-auto"
                    onclick="this.closest('.toast').remove()"></button>
        </div>
    `;
    container.appendChild(toast);

    // Auto-remove after 4 seconds
    setTimeout(() => {
        toast.style.transition = 'opacity .3s';
        toast.style.opacity = '0';
        setTimeout(() => toast.remove(), 300);
    }, 4000);
}

// ─── Load Products from API ─────────────────────────────────────────────────
async function loadProductsFromApi(containerId) {
    const container = document.getElementById(containerId);
    if (!container) return;

    showSpinner();
    try {
        const response = await fetch('/api/products/', {
            headers: {
                'Accept': 'application/json',
            },
            credentials: 'same-origin',
        });

        if (!response.ok) {
            throw new Error(`Ошибка API: ${response.status} ${response.statusText}`);
        }

        const products = await response.json();

        if (products.length === 0) {
            container.innerHTML = `
                <div class="text-center py-5 text-muted">
                    <div style="font-size:3rem;">📦</div>
                    <p class="mt-2">Товары не найдены.</p>
                </div>
            `;
            hideSpinner();
            return;
        }

        container.innerHTML = products.map(product => `
            <div class="col-sm-6 col-md-4 col-lg-4 mb-4">
                <div class="product-card h-100">
                    <div class="card-img-top">
                        ${product.photo
                            ? `<img src="${product.photo}" alt="${product.name}" style="width:100%;height:100%;object-fit:cover;">`
                            : '🎣'
                        }
                    </div>
                    <div class="card-body">
                        <span class="category-badge mb-2">${product.category_name || 'Без категории'}</span>
                        <h5 class="card-title mt-2">${product.name}</h5>
                        <p class="text-muted small">🏭 ${product.manufacturer_name || '—'}</p>
                        <p class="fw-bold fs-4 text-success mb-2">${product.price} руб.</p>
                        <p class="small ${product.stock_quantity > 0 ? 'text-success' : 'text-danger'}">
                            📦 ${product.stock_quantity > 0 ? 'В наличии: ' + product.stock_quantity + ' шт.' : 'Нет в наличии'}
                        </p>
                        <div class="d-flex gap-2">
                            <a href="/catalog/${product.id}/" class="btn btn-outline-primary btn-sm flex-fill">Подробнее</a>
                            ${product.stock_quantity > 0
                                ? `<button class="btn btn-success btn-sm flex-fill"
                                           onclick="addToCartApi(${product.id}, 1)">🛒 В корзину</button>`
                                : `<button class="btn btn-secondary btn-sm flex-fill" disabled>Нет в наличии</button>`
                            }
                        </div>
                    </div>
                </div>
            </div>
        `).join('');

        hideSpinner();
    } catch (error) {
        hideSpinner();
        container.innerHTML = `
            <div class="text-center py-5">
                <div class="alert alert-danger" role="alert">
                    ❌ Не удалось загрузить товары: ${error.message}
                    <br><small>Проверьте подключение или войдите в аккаунт.</small>
                </div>
                <a href="/catalog/" class="btn btn-primary">Открыть каталог</a>
            </div>
        `;
        showToast('Ошибка загрузки товаров: ' + error.message, 'danger');
    }
}

// ─── Add to Cart via API ─────────────────────────────────────────────────────
async function addToCartApi(productId, quantity = 1) {
    showSpinner();
    try {
        const response = await fetch(`/api/cart-items/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            credentials: 'same-origin',
            body: JSON.stringify({
                product: productId,
                quantity: quantity,
            }),
        });

        if (response.status === 403) {
            hideSpinner();
            showToast('Войдите в аккаунт для добавления в корзину', 'warning');
            setTimeout(() => window.location.href = '/login/', 1500);
            return;
        }

        if (!response.ok) {
            const errData = await response.json().catch(() => ({}));
            throw new Error(errData.detail || errData.quantity?.[0] || `Ошибка ${response.status}`);
        }

        hideSpinner();
        showToast('Товар добавлен в корзину!', 'success');

        // Update cart counter in navbar
        updateCartCounter();

    } catch (error) {
        hideSpinner();
        showToast('Ошибка: ' + error.message, 'danger');
    }
}

// ─── Update Cart Counter ─────────────────────────────────────────────────────
async function updateCartCounter() {
    const counter = document.getElementById('cart-counter');
    if (!counter) return;

    try {
        const response = await fetch('/api/carts/', {
            credentials: 'same-origin',
            headers: { 'Accept': 'application/json' },
        });
        if (response.ok) {
            const carts = await response.json();
            if (carts.length > 0) {
                const totalItems = carts[0].items.reduce((sum, item) => sum + item.quantity, 0);
                counter.textContent = totalItems > 0 ? ` (${totalItems})` : '';
            }
        }
    } catch (e) {
        // silently fail
    }
}

// ─── Init on DOM Ready ──────────────────────────────────────────────────────
document.addEventListener('DOMContentLoaded', function () {
    // Load products into API container if exists
    const apiProductsContainer = document.getElementById('api-products-grid');
    if (apiProductsContainer) {
        loadProductsFromApi('api-products-grid');
    }

    // Update cart counter on page load
    updateCartCounter();
});
