from django.db import transaction
from rest_framework import serializers

from .models import (
    Category,
    FoodItem,
    Order,
    OrderItem,
    Payment,
)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "name",
            "description",
            "created_at",
        ]


class FoodItemSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(
        source="category.name",
        read_only=True
    )

    class Meta:
        model = FoodItem
        fields = [
            "id",
            "category",
            "category_name",
            "name",
            "description",
            "price",
            "image",
            "is_available",
            "created_at",
            "updated_at",
        ]


class OrderItemInputSerializer(serializers.Serializer):
    food_item = serializers.IntegerField()
    quantity = serializers.IntegerField(min_value=1)


class OrderCreateSerializer(serializers.Serializer):
    customer_name = serializers.CharField(max_length=100)
    phone_number = serializers.CharField(max_length=15)
    delivery_address = serializers.CharField()
    payment_method = serializers.ChoiceField(
        choices=["CASH", "MPESA"]
    )
    items = OrderItemInputSerializer(many=True)

    def validate_items(self, items):
        if not items:
            raise serializers.ValidationError(
                "Your order must contain at least one item."
            )

        for item in items:
            food_item_id = item["food_item"]

            try:
                food_item = FoodItem.objects.get(
                    id=food_item_id
                )
            except FoodItem.DoesNotExist:
                raise serializers.ValidationError(
                    f"Food item {food_item_id} does not exist."
                )

            if not food_item.is_available:
                raise serializers.ValidationError(
                    f"{food_item.name} is currently unavailable."
                )

        return items

    @transaction.atomic
    def create(self, validated_data):
        items_data = validated_data.pop("items")
        payment_method = validated_data.pop("payment_method")

        order = Order.objects.create(
            **validated_data
        )

        total_amount = 0

        for item_data in items_data:
            food_item = FoodItem.objects.get(
                id=item_data["food_item"],
                is_available=True
            )

            quantity = item_data["quantity"]
            price = food_item.price
            subtotal = price * quantity

            OrderItem.objects.create(
                order=order,
                food_item=food_item,
                quantity=quantity,
                price=price,
                subtotal=subtotal
            )

            total_amount += subtotal

        order.total_amount = total_amount
        order.save()

        Payment.objects.create(
            order=order,
            amount=total_amount,
            payment_method=payment_method
        )

        return order
class OrderResponseSerializer(serializers.ModelSerializer):
    payment_method = serializers.CharField(
        source="payment.payment_method",
        read_only=True
    )

    payment_status = serializers.CharField(
        source="payment.payment_status",
        read_only=True
    )

    class Meta:
        model = Order
        fields = [
            "id",
            "customer_name",
            "phone_number",
            "delivery_address",
            "total_amount",
            "status",
            "payment_method",
            "payment_status",
            "created_at",
        ]
class OrderResponseSerializer(serializers.ModelSerializer):
    payment_method = serializers.CharField(
        source="payment.payment_method",
        read_only=True
    )

    payment_status = serializers.CharField(
        source="payment.payment_status",
        read_only=True
    )

    class Meta:
        model = Order
        fields = [
            "id",
            "customer_name",
            "phone_number",
            "delivery_address",
            "total_amount",
            "status",
            "payment_method",
            "payment_status",
            "created_at",
    ]
class OrderItemResponseSerializer(serializers.ModelSerializer):
    food_item_name = serializers.CharField(
        source="food_item.name",
        read_only=True
    )

    class Meta:
        model = OrderItem
        fields = [
            "id",
            "food_item",
            "food_item_name",
            "quantity",
            "price",
            "subtotal",
        ]
class OrderDetailSerializer(serializers.ModelSerializer):
    items = OrderItemResponseSerializer(
        many=True,
        read_only=True
    )

    payment_method = serializers.CharField(
        source="payment.payment_method",
        read_only=True
    )

    payment_status = serializers.CharField(
        source="payment.payment_status",
        read_only=True
    )

    class Meta:
        model = Order
        fields = [
            "id",
            "customer_name",
            "phone_number",
            "delivery_address",
            "total_amount",
            "status",
            "payment_method",
            "payment_status",
            "items",
            "created_at",
            "updated_at",
        ] 
class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            "status",
        ]