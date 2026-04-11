products = [
    {
        "name": "Laptop",
        "details": {
            "price": 50000,
            "stock": 15,
            "supplier": {"name": "TechCorp", "location": "USA"}
        }
    },
    {
        "name": "Mouse",
        "details": {
            "price": 500,
            "stock": 50,
            "supplier": {"name": "ClickPro", "location": "China"}
        }
    },
    {
        "name": "Keyboard",
        "details": {
            "price": 1500,
            "stock": 5,
            "supplier": {"name": "KeyMakers", "location": "China"}
        }
    },
    {
        "name": "Monitor",
        "details": {
            "price": 12000,
            "stock": 8,
            "supplier": {"name": "ViewBest", "location": "Japan"}
        }
    }
]

def analyze_products(products):
    low_stock_list = []
    high_value_products = []
    out_of_stock = []
    affordable_items_count = 0
    total_inventory_value = 0

    for p in products:
        name = p["name"]
        price = p["details"]["price"]
        stock = p["details"]["stock"] 
        total_value = price * stock

        if stock > 10:
            availability = True
        else:
            availability = False

        p["details"]["in_stock"] = availability

        if stock <= 10:
            low_stock_list.append(name)

        if price > 10000:
            high_value_products.append(name)

        if availability == False:
            out_of_stock.append(name)

        if price < 1000:
            affordable_items_count += 1

        total_inventory_value = total_inventory_value + total_value

    return low_stock_list, high_value_products, out_of_stock, affordable_items_count, total_inventory_value

def display_results(low_stock, high_value, out_of_stock, affordable_count, total_value):
    print(f"Low stock items: {low_stock}")   
    print(f"High value items: {high_value}") 
    print(f"Out of stock items: {out_of_stock}")    
    print(f"Affordable items count: {affordable_count}")
    print(f"Total inventory value: {total_value}")

low_stock, high_value, out_of_stock, affordable_count, total_value = analyze_products(products) 
display_results(low_stock, high_value, out_of_stock, affordable_count, total_value)   

