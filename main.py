products = [
    {"name": "Laptop", "price": 50000, "stock": 15},
    {"name": "Mouse", "price": 500, "stock": 50},
    {"name": "Keyboard", "price": 1500, "stock": 5},
    {"name": "Monitor", "price": 12000, "stock": 8},
    {"name": "USB Cable", "price": 200, "stock": 3}
]

low_stock_list = []
high_value_products = []
affordable_items_count = 0
total_inventory_value = 0

for p in products:
    stock = p["stock"]
    name = p["name"]
    if stock <= 10:
        low_stock_list.append(name)

print(f"Low stock items: {low_stock_list}")

for p in products:
    price = p["price"]
    name = p["name"]
    if price > 10000:
        high_value_products.append(name)

print(f"High value items: {high_value_products}") 

for p in products:
    price = p["price"]
    if price < 1000:
        affordable_items_count = affordable_items_count + 1

print(f"Affordable items count: {affordable_items_count}")

for p in products:
    price = p["price"]
    stock = p["stock"]
    item_total = price * stock
    total_inventory_value = total_inventory_value + item_total

print(f"Total Inventory Value:{total_inventory_value}")