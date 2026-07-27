#!/bin/sh

python manage.py migrate

python manage.py shell <<EOF
from restaurant.models import FoodItem
from django.core.management import call_command

if FoodItem.objects.count() == 0:
    print("Seeding database...")
    call_command("seed")
else:
    print("Database already contains menu items.")
EOF

exec gunicorn config.wsgi