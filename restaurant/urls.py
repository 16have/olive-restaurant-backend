from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    CategoryViewSet,
    FoodItemViewSet,
    OrderCreateView,
    OrderDetailView,
    OrderListView,
    OrderStatusUpdateView,
)

router = DefaultRouter()
router.register(r"categories", CategoryViewSet)
router.register(r"food-items", FoodItemViewSet)

urlpatterns = [
    path("", include(router.urls)),

    path(
        "orders/",
        OrderCreateView.as_view(),
        name="order-create",
    ),

    path(
        "orders/all/",
        OrderListView.as_view(),
        name="order-list",
    ),

    path(
        "orders/<int:pk>/",
        OrderDetailView.as_view(),
        name="order-detail",
    ),

    path(
        "orders/<int:pk>/status/",
        OrderStatusUpdateView.as_view(),
        name="order-status-update",
    ),
]