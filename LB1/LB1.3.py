sales = [
    {"продукт": "яблука", "кількість": 100, "ціна": 5},
    {"продукт": "банани", "кількість": 50, "ціна": 8},
    {"продукт": "яблука", "кількість": 120, "ціна": 5},
    {"продукт": "апельсини", "кількість": 80, "ціна": 12},
    {"продукт": "банани", "кількість": 90, "ціна": 8},
    {"продукт": "груші", "кількість": 30, "ціна": 15}
]

def calculate_revenue(sales_list):
    revenue = {}
    for sale in sales_list:
        product = sale["продукт"]
        total = sale["кількість"] * sale["ціна"]
        revenue[product] = revenue.get(product, 0) + total
    return revenue

total_revenue = calculate_revenue(sales)

top_products = [product for product, income in total_revenue.items() if income > 1000]

print("Загальний дохід по продуктах:", total_revenue)
print("Продукти з доходом понад 1000:", top_products)
