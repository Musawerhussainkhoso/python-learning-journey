#This program sorts orders according to urgency, delivery date, and order value.
from datetime import datetime
def prioritize_orders(
    orders: list[dict]
) -> list[dict]:

    urgency_priority = {
        "critical": 1,
        "high": 2,
        "medium": 3,
        "low": 4
    }

    prioritized_orders = orders.copy()

    prioritized_orders.sort(
        key=lambda order: (
            urgency_priority.get(
                order["urgency"].lower(),
                5
            ),
            datetime.fromisoformat(
                order["delivery_date"]
            ),
            -order["order_value"]
        )
    )

    return prioritized_orders


orders = [
    {
        "order_id": "ORD-101",
        "customer": "Tech Zone",
        "urgency": "High",
        "delivery_date": "2026-07-20",
        "order_value": 250000
    },
    {
        "order_id": "ORD-102",
        "customer": "Digital Mart",
        "urgency": "Critical",
        "delivery_date": "2026-07-18",
        "order_value": 180000
    },
    {
        "order_id": "ORD-103",
        "customer": "Smart Store",
        "urgency": "High",
        "delivery_date": "2026-07-18",
        "order_value": 350000
    },
    {
        "order_id": "ORD-104",
        "customer": "Computer House",
        "urgency": "Low",
        "delivery_date": "2026-07-17",
        "order_value": 500000
    }
]

sorted_orders = prioritize_orders(orders)

print("ORDER PRIORITY REPORT")
print("=" * 75)

for position, order in enumerate(
    sorted_orders,
    start=1
):
    print(f"Priority      : {position}")
    print(f"Order ID      : {order['order_id']}")
    print(f"Customer      : {order['customer']}")
    print(f"Urgency       : {order['urgency']}")
    print(f"Delivery date : {order['delivery_date']}")
    print(f"Value         : Rs. {order['order_value']:,.2f}")
    print("-" * 75)