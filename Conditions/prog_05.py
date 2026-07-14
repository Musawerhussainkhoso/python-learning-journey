'''
This program calculates 
product-wise revenue, region-wise revenue, and the best-selling product.
'''
def generate_sales_report(transactions: list[dict]) -> None:
    product_revenue = {}
    region_revenue = {}
    total_revenue = 0.0

    for transaction in transactions:
        product = transaction["product"]
        region = transaction["region"]
        quantity = transaction["quantity"]
        unit_price = transaction["unit_price"]

        sale_amount = quantity * unit_price
        total_revenue += sale_amount

        product_revenue[product] = (
            product_revenue.get(product, 0) + sale_amount
        )

        region_revenue[region] = (
            region_revenue.get(region, 0) + sale_amount
        )

    print("\nPRODUCT-WISE SALES")
    print("-" * 45)

    for product, revenue in product_revenue.items():
        print(f"{product:<20} Rs. {revenue:>15,.2f}")

    print("\nREGION-WISE SALES")
    print("-" * 45)

    for region, revenue in region_revenue.items():
        print(f"{region:<20} Rs. {revenue:>15,.2f}")

    best_product = ""
    highest_revenue = 0.0

    for product, revenue in product_revenue.items():
        if revenue > highest_revenue:
            highest_revenue = revenue
            best_product = product

    print("-" * 45)
    print(f"Total revenue : Rs. {total_revenue:,.2f}")
    print(f"Best product  : {best_product}")
    print(f"Product sales : Rs. {highest_revenue:,.2f}")


sales_data = [
    {
        "product": "Laptop",
        "region": "Karachi",
        "quantity": 3,
        "unit_price": 150000
    },
    {
        "product": "Monitor",
        "region": "Lahore",
        "quantity": 5,
        "unit_price": 45000
    },
    {
        "product": "Laptop",
        "region": "Islamabad",
        "quantity": 2,
        "unit_price": 150000
    },
    {
        "product": "Keyboard",
        "region": "Karachi",
        "quantity": 15,
        "unit_price": 5000
    },
    {
        "product": "Monitor",
        "region": "Karachi",
        "quantity": 4,
        "unit_price": 45000
    }
]
generate_sales_report(sales_data)
