from django.urls import path

from .views import (
    CategoryListView,
    FoodItemListView,
    OrderCreateView,
    OrderDetailView,
)

urlpatterns = [
    path(
        "categories/",
        CategoryListView.as_view(),
        name="category-list",
    ),

    path(
        "food-items/",
        FoodItemListView.as_view(),
        name="food-item-list",
    ),
    path(
    "orders/",
    OrderCreateView.as_view(),
    name="order-create",
    ),
    path(
    "orders/<int:pk>/",
    OrderDetailView.as_view(),
    name="order-detail",
),
]