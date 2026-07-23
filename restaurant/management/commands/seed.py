from django.core.management.base import BaseCommand
from restaurant.models import (
    Category,
    FoodItem,
    Order,
    OrderItem,
    Payment,
)


class Command(BaseCommand):
    help = "Seed the database with sample restaurant data"

    def handle(self, *args, **kwargs):

        # Delete dependent records first
        Payment.objects.all().delete()
        OrderItem.objects.all().delete()
        Order.objects.all().delete()

        # Then delete menu data
        FoodItem.objects.all().delete()
        Category.objects.all().delete()

        # Create categories
        main = Category.objects.create(
            name="Main Meals",
            description="Our signature dishes",
        )

        fast_food = Category.objects.create(
            name="Fast Food",
            description="Quick bites",
        )

        drinks = Category.objects.create(
            name="Drinks",
            description="Refreshing beverages",
        )

        desserts = Category.objects.create(
            name="Desserts",
            description="Sweet treats",
        )

        # Create food items
        FoodItem.objects.bulk_create([
            FoodItem(
                category=main,
                name="Chicken Biryani",
                description="Served with fresh salad",
                price=850,
                image="food_images/biryani.jpg",
                is_available=True,
            ),
            FoodItem(
                category=main,
                name="Beef Pilau",
                description="Traditional Kenyan pilau",
                price=650,
                image="food_images/pilau.jpg",
                is_available=True,
            ),
            FoodItem(
                category=fast_food,
                name="Chicken Burger",
                description="With fries",
                price=700,
                image="food_images/burger.jpg",
                is_available=True,
            ),
            FoodItem(
                category=fast_food,
                name="Chips Masala",
                description="Spicy chips",
                price=350,
                image="food_images/chips.jpg",
                is_available=True,
            ),
            FoodItem(
                category=drinks,
                name="Fresh Orange Juice",
                description="Freshly squeezed",
                price=300,
                image="food_images/orange.jpg",
                is_available=True,
            ),
            FoodItem(
                category=drinks,
                name="Mango Smoothie",
                description="Fresh mango blend",
                price=400,
                image="food_images/mango.jpg",
                is_available=True,
            ),
            FoodItem(
                category=desserts,
                name="Chocolate Cake",
                description="Rich chocolate slice",
                price=450,
                image="food_images/cake.jpg",
                is_available=True,
            ),
            FoodItem(
                category=desserts,
                name="Ice Cream",
                description="Vanilla scoop",
                price=250,
                image="food_images/icecream.jpg",
                is_available=True,
            ),
        ])


        self.stdout.write(
            self.style.SUCCESS("Restaurant seeded successfully!")
        )