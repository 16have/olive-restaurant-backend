from rest_framework import generics

from .models import Category, FoodItem
from .serializers import (
    CategorySerializer,
    FoodItemSerializer,
)


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class FoodItemListView(generics.ListAPIView):
    queryset = FoodItem.objects.filter(
        is_available=True
    )
    serializer_class = FoodItemSerializer