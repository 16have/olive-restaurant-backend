from rest_framework import generics, status
from rest_framework.response import Response

from .models import Category, FoodItem, Order
from .serializers import (
    CategorySerializer,
    FoodItemSerializer,
    OrderCreateSerializer,
    OrderResponseSerializer,
    OrderDetailSerializer,
)


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class FoodItemListView(generics.ListAPIView):
    queryset = FoodItem.objects.filter(
        is_available=True
    )
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
class OrderDetailView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderDetailSerializer    