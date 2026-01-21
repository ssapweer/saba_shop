from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='shop'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    # ВОТ ЭТА СТРОКА ДОЛЖНА БЫТЬ ТУТ:
    path('product/<int:pk>/add_review/', views.add_review, name='add_review'),

    path('my-manage-panel/', views.my_admin, name='my_admin'),
    path('my-manage-panel/add/', views.add_product, name='product_create'),
    path('my-manage-panel/delete/<int:pk>/', views.delete_product, name='product_delete'),
    path('promotions/', views.promotions, name='promotions'),
    path('login/', views.login, name='login'),
]