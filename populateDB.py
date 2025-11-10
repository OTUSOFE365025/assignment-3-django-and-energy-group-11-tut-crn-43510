############################################################################
## Django ORM Standalone Script: Populate Database
############################################################################

import sys
import os

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
import django
django.setup()

# Import Product model
from db.models import Product


def populate_products():
    """Populate the database with sample product data."""
    products = [
        {"upc": "123456789012", "name": "Apple", "price": 0.99},
        {"upc": "987654321098", "name": "Banana", "price": 0.79},
        {"upc": "111222333444", "name": "Milk", "price": 2.49},
        {"upc": "555666777888", "name": "Bread", "price": 3.19},
        {"upc": "999888777666", "name": "Eggs", "price": 4.29},
        {"upc": "333444555666", "name": "Orange Juice", "price": 3.99},
        {"upc": "444555666777", "name": "Cheddar Cheese", "price": 5.49},
        {"upc": "222333444555", "name": "Chicken Breast", "price": 6.99},
        {"upc": "888999000111", "name": "Ground Beef", "price": 7.49},
        {"upc": "777888999000", "name": "Pasta", "price": 1.49},
        {"upc": "666777888999", "name": "Tomato Sauce", "price": 2.29},
        {"upc": "555444333222", "name": "Rice", "price": 3.79},
        {"upc": "112233445566", "name": "Butter", "price": 4.59},
        {"upc": "223344556677", "name": "Yogurt", "price": 1.29},
        {"upc": "334455667788", "name": "Cereal", "price": 4.49},
        {"upc": "445566778899", "name": "Chips", "price": 3.69},
        {"upc": "556677889900", "name": "Soda", "price": 2.19},
        {"upc": "667788990011", "name": "Bottled Water", "price": 1.09},
        {"upc": "778899001122", "name": "Toilet Paper", "price": 5.99},
        {"upc": "889900112233", "name": "Paper Towels", "price": 4.79},
        {"upc": "990011223344", "name": "Dish Soap", "price": 3.29},
        {"upc": "101112131415", "name": "Coffee", "price": 8.49},
        {"upc": "121314151617", "name": "Tea", "price": 4.19},
        {"upc": "131415161718", "name": "Frozen Pizza", "price": 6.49},
        {"upc": "141516171819", "name": "Ice Cream", "price": 5.99}
    ]


    for p in products:
        Product.objects.get_or_create(
            upc=p["upc"], defaults={"name": p["name"], "price": p["price"]}
        )
    print("✅ Database populated with products.")


