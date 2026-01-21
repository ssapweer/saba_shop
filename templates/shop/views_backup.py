from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from .models import Product
from .forms import ProductForm

# ВАЖНО: Импортируем форму и модель из другого приложения правильно
from shop.forms import ReviewForm

def is_admin(user):
    return user.is_authenticated and user.is_superuser

# Главная страница
def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/index.html', {'products': products})

# Страница товара + Отзывы
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    reviews = product.reviews.all()
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.save()
            return redirect('product_detail', pk=pk)
    else:
        form = ReviewForm()
    return render(request, 'shop/product_detail.html', {
        'product': product,
        'reviews': reviews,
        'form': form
    })

# Твоя админка
@user_passes_test(is_admin, login_url='/login/')
def my_admin_panel(request):
    products = Product.objects.all()
    return render(request, 'shop/admin_panel.html', {'products': products})

# Создание
@user_passes_test(is_admin, login_url='/login/')
def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my_admin')
    else:
        form = ProductForm()
    return render(request, 'shop/product_form.html', {'form': form})

# Удаление
@user_passes_test(is_admin, login_url='/login/')
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('my_admin')