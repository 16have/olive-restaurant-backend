from django.urls import path

from .views import (
    CategoryListView,
    FoodItemListView,
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
]