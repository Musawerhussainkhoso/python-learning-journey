#4. Calculate Total Revenue from Products
products = [
    {"name": "Laptop", "price": 70000, "sold": 10},
    {"name": "Phone", "price": 30000, "sold": 15},
    {"name": "Tablet", "price": 25000, "sold": 8}
]

revenues = list(
    map(lambda p: p["price"] * p["sold"], products)
)

for product, revenue in zip(products, revenues):
    print(product["name"], "Revenue =", revenue)

print("Total Revenue =", sum(revenues))