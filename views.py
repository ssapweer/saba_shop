from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    API для работы с товарами (Products Service - Проект A)

    GET /api/products/ - получить список всех товаров
    GET /api/products/{id}/ - получить товар по ID
    POST /api/products/ - создать новый товар
    PUT /api/products/{id}/ - обновить товар
    DELETE /api/products/{id}/ - удалить товар
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        """
        Получить список всех активных товаров
        """
        print("🔵 Products Service: Получен запрос на список товаров")
        queryset = self.get_queryset().filter(is_active=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        """
        Получить товар по ID
        """
        product_id = kwargs.get('pk')
        print(f"🔵 Products Service: Получен запрос на товар ID={product_id}")

        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            print(f"✅ Products Service: Товар найден - {instance.name}")
            return Response(serializer.data)
        except Product.DoesNotExist:
            print(f"❌ Products Service: Товар ID={product_id} не найден")
            return Response(
                {"error": "Товар не найден"},
                status=status.HTTP_404_NOT_FOUND
            )