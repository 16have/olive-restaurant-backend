from django.urls import path

from .views import (
    CategoryListView,
    FoodItemListView,
    OrderCreateView,
    OrderDetailView,
    OrderStatusUpdateView,
    create_admin,
    AdminLoginView, 
    OrderListView, 
    FoodItemCreateView, 
    FoodItemUpdateDeleteView
)

urlpatterns = [
    path("categories/", CategoryListView.as_view(), name="category-list"),
    path("food-items/", FoodItemListView.as_view(), name="food-item-list"),
    path("orders/", OrderCreateView.as_view(), name="order-create"),
    path("orders/<int:pk>/", OrderDetailView.as_view(), name="order-detail"),
    path("orders/<int:pk>/status/", OrderStatusUpdateView.as_view(), name="order-status-update"),
    path("create-admin/", create_admin, name="create-admin"),
    path("admin-login/", AdminLoginView.as_view(), name="admin-login"),
    path("admin/orders/", OrderListView.as_view(), name="admin-order-list"),
    path("admin/food-items/", FoodItemCreateView.as_view(), name="admin-food-create"),
    path("admin/food-items/<int:pk>/", FoodItemUpdateDeleteView.as_view(), name="admin-food-detail"),
]