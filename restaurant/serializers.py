from rest_framework import serializers
from .models import Category, FoodItem 

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
    items = OrderItemInputSerializer(
        many=True
    )

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