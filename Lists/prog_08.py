#This program compares the inventory stored in software with the physical stock available in a warehouse.
def reconcile_inventory(
    system_inventory: list[dict],
    physical_inventory: list[dict]
) -> list[dict]:

    physical_stock = {}

    for product in physical_inventory:
        physical_stock[product["product_code"]] = product[
            "physical_quantity"
        ]

    reconciliation_report = []

    for product in system_inventory:
        product_code = product["product_code"]
        system_quantity = product["system_quantity"]

        physical_quantity = physical_stock.get(
            product_code,
            0
        )

        difference = physical_quantity - system_quantity

        if difference == 0:
            status = "Matched"
        elif difference > 0:
            status = "Extra physical stock"
        else:
            status = "Stock shortage"

        reconciliation_report.append({
            "product_code": product_code,
            "product_name": product["product_name"],
            "system_quantity": system_quantity,
            "physical_quantity": physical_quantity,
            "difference": difference,
            "status": status
        })

    return reconciliation_report


system_stock = [
    {
        "product_code": "P101",
        "product_name": "Wireless Mouse",
        "system_quantity": 50
    },
    {
        "product_code": "P102",
        "product_name": "Mechanical Keyboard",
        "system_quantity": 30
    },
    {
        "product_code": "P103",
        "product_name": "USB-C Hub",
        "system_quantity": 20
    }
]

physical_stock = [
    {
        "product_code": "P101",
        "physical_quantity": 48
    },
    {
        "product_code": "P102",
        "physical_quantity": 30
    },
    {
        "product_code": "P103",
        "physical_quantity": 25
    }
]

report = reconcile_inventory(
    system_stock,
    physical_stock
)
print("INVENTORY RECONCILIATION REPORT")
print("=" * 80)
for item in report:
    print(f"Product    : {item['product_name']}")
    print(f"System     : {item['system_quantity']}")
    print(f"Physical   : {item['physical_quantity']}")
    print(f"Difference : {item['difference']}")
    print(f"Status     : {item['status']}")
    print("-" * 80)