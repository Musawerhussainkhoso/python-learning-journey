'''
This program manages product stock, processes sales,
updates inventory, and identifies low-stock products.
'''
from typing import Dict
Product = Dict[str, object]
def process_sale(
    inventory: Dict[str, Product],
    product_code: str,
    quantity: int
) -> bool:

    if product_code not in inventory:
        print(f"Product code '{product_code}' does not exist.")
        return False

    if quantity <= 0:
        print("Sale quantity must be greater than zero.")
        return False

    available_stock = int(inventory[product_code]["stock"])

    if quantity > available_stock:
        print(
            f"Insufficient stock. Available quantity: "
            f"{available_stock}"
        )
        return False

    inventory[product_code]["stock"] = available_stock - quantity

    unit_price = float(inventory[product_code]["price"])
    total_amount = quantity * unit_price

    print("\nSale completed successfully.")
    print(f"Product      : {inventory[product_code]['name']}")
    print(f"Quantity     : {quantity}")
    print(f"Total amount : Rs. {total_amount:,.2f}")

    return True


def display_low_stock_products(
    inventory: Dict[str, Product],
    stock_limit: int = 10
) -> None:

    print("\nLOW-STOCK PRODUCTS")
    print("-" * 55)

    low_stock_found = False

    for product_code, product in inventory.items():
        current_stock = int(product["stock"])

        if current_stock <= stock_limit:
            low_stock_found = True

            print(f"Code  : {product_code}")
            print(f"Name  : {product['name']}")
            print(f"Stock : {current_stock}")
            print("-" * 55)

    if not low_stock_found:
        print("All products have sufficient stock.")


def calculate_inventory_value(
    inventory: Dict[str, Product]
) -> float:

    total_value = 0.0

    for product in inventory.values():
        stock = int(product["stock"])
        price = float(product["price"])

        total_value += stock * price

    return total_value


inventory = {
    "P-1001": {
        "name": "Wireless Keyboard",
        "category": "Computer Accessories",
        "price": 4500.00,
        "stock": 25
    },
    "P-1002": {
        "name": "Gaming Mouse",
        "category": "Computer Accessories",
        "price": 3200.00,
        "stock": 8
    },
    "P-1003": {
        "name": "USB-C Hub",
        "category": "Electronics",
        "price": 5500.00,
        "stock": 15
    },
    "P-1004": {
        "name": "Laptop Stand",
        "category": "Office Equipment",
        "price": 2800.00,
        "stock": 5
    }
}


process_sale(inventory, "P-1001", 4)

display_low_stock_products(inventory)

inventory_value = calculate_inventory_value(inventory)

print(
    f"\nCurrent inventory value: "
    f"Rs. {inventory_value:,.2f}"
)
