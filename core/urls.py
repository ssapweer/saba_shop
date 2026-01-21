from django.contrib import admin
from django.urls import path
from shop import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='shop'),
    path('promotions/', views.promotions, name='promotions'),

    # КОРЗИНА
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:pk>/', views.add_to_cart, name='add_to_cart'),

    # ТОВАРЫ И ОТЗЫВЫ
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('product/<int:pk>/add_review/', views.add_review, name='add_review'),

    # ПАНЕЛЬ УПРАВЛЕНИЯ
    path('my-manage-panel/', views.my_admin, name='my_admin'),
    path('my-manage-panel/add/', views.add_product, name='add_product'),
    path('my-manage-panel/edit/<int:pk>/', views.edit_product, name='edit_product'),
    path('my-manage-panel/delete/<int:pk>/', views.delete_product, name='delete_product'),

    path('login/', views.login_view, name='login'),  # переименовал во избежание конфликтов
    path('cart/remove/<int:pk>/', views.remove_from_cart, name='remove_from_cart'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
