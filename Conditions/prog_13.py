#This program processes an order, calculates item totals, discounts, tax, and final payable amount.
def generate_invoice(
    customer_name: str,
    cart: list[dict]
) -> None:

    subtotal = 0.0
    total_items = 0

    print("\nCUSTOMER INVOICE")
    print("=" * 80)
    print(f"Customer: {customer_name}")
    print("-" * 80)

    print(
        f"{'Product':<25}"
        f"{'Quantity':<12}"
        f"{'Price':<18}"
        f"{'Total':<18}"
    )

    print("-" * 80)

    for item in cart:
        product = item["product"]
        quantity = item["quantity"]
        unit_price = item["unit_price"]

        item_total = quantity * unit_price

        subtotal += item_total
        total_items += quantity

        print(
            f"{product:<25}"
            f"{quantity:<12}"
            f"Rs. {unit_price:<14,.2f}"
            f"Rs. {item_total:<14,.2f}"
        )

    if subtotal >= 300000:
        discount_rate = 0.15
    elif subtotal >= 150000:
        discount_rate = 0.10
    elif subtotal >= 50000:
        discount_rate = 0.05
    else:
        discount_rate = 0.0

    discount_amount = subtotal * discount_rate
    discounted_total = subtotal - discount_amount

    tax_rate = 0.05
    tax_amount = discounted_total * tax_rate

    final_amount = discounted_total + tax_amount

    print("-" * 80)
    print(f"Total items       : {total_items}")
    print(f"Subtotal          : Rs. {subtotal:,.2f}")
    print(f"Discount rate     : {discount_rate * 100:.0f}%")
    print(f"Discount amount   : Rs. {discount_amount:,.2f}")
    print(f"Tax amount        : Rs. {tax_amount:,.2f}")
    print(f"Final amount      : Rs. {final_amount:,.2f}")
    print("=" * 80)


shopping_cart = [
    {
        "product": "Laptop",
        "quantity": 1,
        "unit_price": 175000
    },
    {
        "product": "Wireless Mouse",
        "quantity": 2,
        "unit_price": 4500
    },
    {
        "product": "External SSD",
        "quantity": 1,
        "unit_price": 28000
    },
    {
        "product": "Laptop Bag",
        "quantity": 1,
        "unit_price": 7500
    }
]
generate_invoice("Abdul Majid", shopping_cart)