'''
This program takes sales transactions and creates reports by region and product.
'''
from typing import Dict, List
Transaction = Dict[str, object]
def analyse_sales(
    transactions: List[Transaction]
) -> None:

    sales_by_region: Dict[str, float] = {}
    sales_by_product: Dict[str, float] = {}
    quantity_by_product: Dict[str, int] = {}

    for transaction in transactions:
        region = str(transaction["region"])
        product = str(transaction["product"])
        quantity = int(transaction["quantity"])
        unit_price = float(transaction["unit_price"])

        total_sale = quantity * unit_price

        sales_by_region[region] = (
            sales_by_region.get(region, 0.0) + total_sale
        )

        sales_by_product[product] = (
            sales_by_product.get(product, 0.0) + total_sale
        )

        quantity_by_product[product] = (
            quantity_by_product.get(product, 0) + quantity
        )

    sorted_regions = sorted(
        sales_by_region.items(),
        key=lambda item: item[1],
        reverse=True
    )

    sorted_products = sorted(
        sales_by_product.items(),
        key=lambda item: item[1],
        reverse=True
    )

    print("\nSALES BY REGION")
    print("-" * 50)

    for region, amount in sorted_regions:
        print(f"{region:<15} Rs. {amount:>15,.2f}")

    print("\nSALES BY PRODUCT")
    print("-" * 50)

    for product, amount in sorted_products:
        quantity = quantity_by_product[product]

        print(
            f"{product:<20} "
            f"Quantity: {quantity:<5} "
            f"Sales: Rs. {amount:,.2f}"
        )

    if sorted_products:
        best_product, highest_sales = sorted_products[0]

        print(
            f"\nBest-selling product by revenue: "
            f"{best_product} — Rs. {highest_sales:,.2f}"
        )


transactions = [
    {
        "transaction_id": "T001",
        "region": "Karachi",
        "product": "Laptop",
        "quantity": 3,
        "unit_price": 150000
    },
    {
        "transaction_id": "T002",
        "region": "Lahore",
        "product": "Monitor",
        "quantity": 5,
        "unit_price": 45000
    },
    {
        "transaction_id": "T003",
        "region": "Karachi",
        "product": "Monitor",
        "quantity": 2,
        "unit_price": 45000
    },
    {
        "transaction_id": "T004",
        "region": "Islamabad",
        "product": "Laptop",
        "quantity": 2,
        "unit_price": 150000
    },
    {
        "transaction_id": "T005",
        "region": "Lahore",
        "product": "Keyboard",
        "quantity": 15,
        "unit_price": 5000
    },
    {
        "transaction_id": "T006",
        "region": "Karachi",
        "product": "Keyboard",
        "quantity": 10,
        "unit_price": 5000
    }
]
analyse_sales(transactions)
