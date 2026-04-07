products = [
    {"name": "Laptop", "price": 50000, "stock": 15},
    {"name": "Mouse", "price": 500, "stock": 50},
    {"name": "Keyboard", "price": 1500, "stock": 5},
    {"name": "Monitor", "price": 12000, "stock": 8},
    {"name": "USB Cable", "price": 200, "stock": 3}
]

def analyze_products(products):

    low_stock_list = []
    high_value_products = []
    affordable_items_count = 0
    total_inventory_value = 0   

    for p in products:
        stock = p["stock"]
        name = p["name"]
        price = p["price"]
        item_total = price * stock
        
        if stock <= 10:
            low_stock_list.append(name)

        if price > 10000:
            high_value_products.append(name) 

        if price < 1000:
            affordable_items_count = affordable_items_count + 1
       
        total_inventory_value = total_inventory_value + item_total

    return low_stock_list, high_value_products, affordable_items_count, total_inventory_value

def display_results(low_stock_list, high_value_products, affordable_items_count, total_inventory_value):
    print(f"Low stock items: {low_stock_list}")
    print(f"High value items: {high_value_products}")
    print(f"Affordable items count: {affordable_items_count}")
    print(f"Total Inventory Value: {total_inventory_value}")

low_stock, high_value, affordable_count, total_value = analyze_products(products)
display_results(low_stock, high_value, affordable_count, total_value)










    
