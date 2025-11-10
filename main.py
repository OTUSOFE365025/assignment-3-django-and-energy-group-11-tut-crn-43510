############################################################################
## Django ORM Standalone Python Template
############################################################################
""" Here we'll import the parts of Django we need. It's recommended to leave
these settings as is, and skip to START OF APPLICATION section below """

# Turn off bytecode generation
import sys
sys.dont_write_bytecode = True

# Import settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

# setup django environment
import django
django.setup()

# Import your models for use in your script
from db.models import *

############################################################################
## START OF APPLICATION
############################################################################
""" Cash Register - Django ORM Implementation """

from db.models import Product
from populateDB import populate_products


# --- Scanning UI ---
def scan_product():
    upc = input("Enter Product UPC: ")

    if upc.lower() == "exit":
        print("Exiting scan.")
        sys.exit()
    try:
        product = Product.objects.get(upc=upc)
        print(f"Scanned Product: {product.name} - ${product.price}\n")
    except Product.DoesNotExist:
        print("Error: Product not found.\n")


if __name__ == "__main__":
    populate_products()
    print("\n--- Scan Product ---")
    print("Enter 'exit' to quit.\n")
    while True:
        scan_product()
