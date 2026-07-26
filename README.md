# 🍽️ Olive Restaurant Backend

A Django REST Framework backend powering the Olive Restaurant food ordering and delivery application.

## Project Overview

Olive Restaurant Backend provides a RESTful API for managing restaurant menu items, customer orders, payments, and order tracking. The system is designed to support a React frontend while allowing administrators to manage restaurant operations through the Django Admin panel.

---

## Features

### Customer Features

* View food categories
* Browse available menu items
* Place food orders
* Track order status
* Choose payment method
* View order details

### Admin Features

* Secure Django Admin authentication
* Manage menu categories
* Manage food items
* View customer orders
* Update order status
* View payment information

---

## Tech Stack

* Python 3.14
* Django 6
* Django REST Framework
* SQLite (Development)
* Docker
* GitHub Actions

---

## Database Models

The application consists of five main models:

* Category
* FoodItem
* Order
* OrderItem
* Payment

Relationships:

```text
Category
   │
   └── FoodItem
            │
            └── OrderItem
                        │
                        └── Order
                               │
                               └── Payment
```

---

## API Endpoints

### Categories

| Method | Endpoint           |
| ------ | ------------------ |
| GET    | `/api/categories/` |

---

### Food Items

| Method | Endpoint           |
| ------ | ------------------ |
| GET    | `/api/food-items/` |

---

### Orders

| Method | Endpoint                   |
| ------ | -------------------------- |
| POST   | `/api/orders/`             |
| GET    | `/api/orders/<id>/`        |
| GET    | `/api/orders/all/`         |
| PATCH  | `/api/orders/<id>/status/` |

---

## Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/olive-restaurant-backend.git
```

Navigate into the project

```bash
cd olive-restaurant-backend
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

macOS/Linux

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run migrations

```bash
python manage.py migrate
```

Seed the database

```bash
python manage.py seed
```

Start the development server

```bash
python manage.py runserver
```

---

## Docker

Build the image

```bash
docker build -t olive-backend .
```

Run the container

```bash
docker run -p 8000:8000 olive-backend
```

---

## Django Admin

Create a superuser

```bash
python manage.py createsuperuser
```

Login

```
http://127.0.0.1:8000/admin/
```

---

## GitHub Actions

Continuous Integration automatically runs:

* Django project checks
* Dependency installation
* Build validation

---

## Future Improvements

* JWT Authentication
* MPESA API Integration
* Rider Management
* Inventory Management
* Customer Reviews
* Favorites/Wishlist
* Notifications
* Analytics Dashboard

---

## Author

Kelvin Tullo

---

## License

This project was developed for educational and portfolio purposes.
