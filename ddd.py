from products.models import Product  # <-- replace 'products' with your app name
import random
import string

# Function to generate random SKU
def random_sku(length=8):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

products = []

# --- Electronics ---
for i in range(1, 11):
    products.append({
        "name": f"Electronics Gadget {i}",
        "price": round(random.uniform(1000, 20000), 2),
        "stock": random.randint(5, 50),
        "sku": random_sku(),
        "description": f"High quality electronics item number {i}",
        "is_active": True,
        "category": "electronics"
    })

# --- Clothes ---
for i in range(1, 11):
    products.append({
        "name": f"Clothes Item {i}",
        "price": round(random.uniform(500, 10000), 2),
        "stock": random.randint(10, 50),
        "sku": random_sku(),
        "description": f"Stylish and comfortable clothing item {i}",
        "is_active": True,
        "category": "clothes"
    })

# --- Grocery ---
for i in range(1, 11):
    products.append({
        "name": f"Grocery Product {i}",
        "price": round(random.uniform(100, 2000), 2),
        "stock": random.randint(20, 100),
        "sku": random_sku(),
        "description": f"Fresh and quality grocery product {i}",
        "is_active": True,
        "category": "grocery"
    })

# --- Mobile ---
for i in range(1, 11):
    products.append({
        "name": f"Mobile Device {i}",
        "price": round(random.uniform(10000, 150000), 2),
        "stock": random.randint(5, 20),
        "sku": random_sku(),
        "description": f"High-end mobile phone model {i}",
        "is_active": True,
        "category": "mobile"
    })

# --- Furniture ---
for i in range(1, 11):
    products.append({
        "name": f"Furniture Item {i}",
        "price": round(random.uniform(5000, 50000), 2),
        "stock": random.randint(5, 15),
        "sku": random_sku(),
        "description": f"Elegant and durable furniture item {i}",
        "is_active": True,
        "category": "furniture"
    })

# --- TV & Appliances ---
for i in range(1, 11):
    products.append({
        "name": f"TV & Appliance {i}",
        "price": round(random.uniform(10000, 80000), 2),
        "stock": random.randint(5, 20),
        "sku": random_sku(),
        "description": f"High quality TV & appliance {i}",
        "is_active": True,
        "category": "tv"
    })

# --- Beauty & Food ---
for i in range(1, 11):
    products.append({
        "name": f"Beauty & Food {i}",
        "price": round(random.uniform(200, 5000), 2),
        "stock": random.randint(10, 50),
        "sku": random_sku(),
        "description": f"Top quality beauty or food product {i}",
        "is_active": True,
        "category": "beauty"
    })

# Bulk create in shell
Product.objects.bulk_create([Product(**p) for p in products])
