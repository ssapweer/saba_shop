from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, CartItem

# --- ГЛАВНАЯ И АКЦИИ ---
def index(request):
    products = Product.objects.all()
    return render(request, 'shop/index.html', {'products': products})

def promotions(request):
    return render(request, 'shop/promotions.html')

# --- КОРЗИНА (ПЛЮС, МИНУС, ПРОСМОТР) ---
def cart_detail(request):
    items = CartItem.objects.all()
    total = sum(item.total_price() for item in items)
    return render(request, 'shop/cart.html', {'items': items, 'total': total})

def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart_item, created = CartItem.objects.get_or_create(product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect(request.META.get('HTTP_REFERER', 'shop'))

def remove_from_cart(request, pk):
    cart_item = get_object_or_404(CartItem, pk=pk)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart_detail')

# --- ТОВАР И ОТЗЫВЫ (РЕШАЕМ ОШИБКУ) ---
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'shop/product_detail.html', {'product': product})

def add_review(request, pk):
    return redirect('product_detail', pk=pk)

# --- ВХОД (РЕШАЕМ ОШИБКУ) ---
def login_view(request):
    return render(request, 'registration/login.html')

# --- АДМИНКА (УПРАВЛЕНИЕ) ---
def my_admin(request):
    products = Product.objects.all()
    return render(request, 'shop/my_admin.html', {'products': products})

def add_product(request):
    if request.method == "POST":
        Product.objects.create(
            name=request.POST.get('name'),
            description=request.POST.get('description'),
            price=request.POST.get('price'),
            image_url=request.POST.get('image_url')
        )
        return redirect('my_admin')
    return render(request, 'shop/add_product.html')


def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product.name = request.POST.get('name')
        product.description = request.POST.get('description')

        # Проверяем цену: если пришла пустая строка, ставим 0
        price_val = request.POST.get('price')
        product.price = price_val if price_val and price_val.strip() else 0

        product.image_url = request.POST.get('image_url')
        product.save()
        return redirect('my_admin')
    return render(request, 'shop/edit_product.html', {'product': product})

def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('my_admin')