import os
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework import generics, status
from rest_framework.response import Response

from .models import Category, FoodItem, Order
from .serializers import (
    CategorySerializer,
    FoodItemSerializer,
    OrderCreateSerializer,
    OrderResponseSerializer,
    OrderDetailSerializer,
    OrderStatusSerializer,
)


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class FoodItemListView(generics.ListAPIView):
    queryset = FoodItem.objects.filter(is_available=True)
    serializer_class = FoodItemSerializer


class OrderCreateView(generics.CreateAPIView):
    serializer_class = OrderCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        order = serializer.save()

        response_serializer = OrderResponseSerializer(order)

        return Response(
            response_serializer.data,
            status=status.HTTP_201_CREATED
        )


class OrderListView(generics.ListAPIView):
    """Admin: view all orders."""
    queryset = Order.objects.all().order_by("-created_at")
    serializer_class = OrderDetailSerializer


class OrderDetailView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderDetailSerializer


class OrderStatusUpdateView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderStatusSerializer
    http_method_names = ["patch"]


def create_admin(request):
    """
    TEMPORARY endpoint — creates a superuser on the deployed database when
    shell access isn't available. Remove this route once you've logged in
    and created real admin data.
    """
    if User.objects.filter(username="admin").exists():
        return JsonResponse({"message": "Admin already exists."})

    User.objects.create_superuser(
        username="admin",
        email="admin@example.com",
        password=os.environ.get("SEED_ADMIN_PASSWORD", "changeme123"),
    )
    return JsonResponse({"message": "Superuser created successfully."})