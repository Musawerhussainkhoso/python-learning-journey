#This is similar to an SQL LEFT JOIN. Every customer appears even when they have no orders.
def generate_customer_order_summary(
    customers: list[dict],
    orders: list[dict]
) -> list[dict]:

    order_summary = {}

    for order in orders:
        customer_id = order["customer_id"]

        if customer_id not in order_summary:
            order_summary[customer_id] = {
                "number_of_orders": 0,
                "total_spent": 0.0,
                "order_ids": []
            }

        order_summary[customer_id][
            "number_of_orders"
        ] += 1

        order_summary[customer_id][
            "total_spent"
        ] += order["amount"]

        order_summary[customer_id][
            "order_ids"
        ].append(order["order_id"])

    customer_report = []

    for customer in customers:
        customer_id = customer["customer_id"]

        summary = order_summary.get(
            customer_id,
            {
                "number_of_orders": 0,
                "total_spent": 0.0,
                "order_ids": []
            }
        )

        customer_report.append({
            "customer_id": customer_id,
            "customer_name": customer["name"],
            "city": customer["city"],
            "number_of_orders": summary[
                "number_of_orders"
            ],
            "total_spent": summary["total_spent"],
            "order_ids": summary["order_ids"]
        })

    return customer_report


customers = [
    {
        "customer_id": 101,
        "name": "Ali Khan",
        "city": "Karachi"
    },
    {
        "customer_id": 102,
        "name": "Sara Ahmed",
        "city": "Lahore"
    },
    {
        "customer_id": 103,
        "name": "Hamza Ali",
        "city": "Hyderabad"
    }
]

orders = [
    {
        "order_id": "ORD-1",
        "customer_id": 101,
        "amount": 25000
    },
    {
        "order_id": "ORD-2",
        "customer_id": 101,
        "amount": 45000
    },
    {
        "order_id": "ORD-3",
        "customer_id": 102,
        "amount": 18000
    }
]

customer_summary = generate_customer_order_summary(
    customers,
    orders
)

print("CUSTOMER ORDER SUMMARY")
print("=" * 65)

for customer in customer_summary:
    print(f"Customer      : {customer['customer_name']}")
    print(f"City          : {customer['city']}")
    print(
        f"Total orders  : "
        f"{customer['number_of_orders']}"
    )
    print(
        f"Total spent   : "
        f"Rs. {customer['total_spent']:,.2f}"
    )
    print(f"Order IDs     : {customer['order_ids']}")
    print("-" * 65)