products = [
    {"name": "Стол", "price": 5000, "discount": 10},
    {"name": "Стул", "price": 1500, "discount": 5},
    {"name": "Шкаф", "price": 20000, "discount": 15},
    {"name": "Диван", "price": 40000, "discount": 7},
    {"name": "Полка", "price": 2500, "discount": 12},
]

print("Чек на покупки в магазине мебели")
print("-" * 40)

amount = 0

for product in products:
    total_price = product["price"] * (100 - product["discount"]) / 100
    amount += total_price
    print(f"{product['name']:15} {product['price']}p - {product['discount']}% = {total_price: .2f}p")

print("-" * 40)
print(f"Итоговая сумма: {amount:.2f}p")