'''
A customer may appear multiple times with the same email.
This program keeps only the most recently updated record.
'''
from datetime import datetime
def remove_duplicate_customers(
    customer_records: list[dict]
) -> list[dict]:

    latest_records = {}

    for customer in customer_records:
        email = customer["email"].strip().lower()
        updated_at = datetime.fromisoformat(customer["updated_at"])

        customer["email"] = email

        if email not in latest_records:
            latest_records[email] = customer
            continue

        previous_date = datetime.fromisoformat(
            latest_records[email]["updated_at"]
        )

        if updated_at > previous_date:
            latest_records[email] = customer

    cleaned_customers = list(latest_records.values())

    cleaned_customers.sort(
        key=lambda customer: customer["customer_id"]
    )

    return cleaned_customers


customers = [
    {
        "customer_id": 101,
        "name": "Ali Khan",
        "email": "ALI@GMAIL.COM",
        "city": "Karachi",
        "updated_at": "2026-07-01T10:30:00"
    },
    {
        "customer_id": 102,
        "name": "Sara Ahmed",
        "email": "sara@gmail.com",
        "city": "Lahore",
        "updated_at": "2026-07-02T09:00:00"
    },
    {
        "customer_id": 101,
        "name": "Ali Khan",
        "email": "ali@gmail.com",
        "city": "Hyderabad",
        "updated_at": "2026-07-05T14:45:00"
    }
]

cleaned_data = remove_duplicate_customers(customers)

print("LATEST CUSTOMER RECORDS")
print("-" * 60)

for customer in cleaned_data:
    print(
        f"{customer['customer_id']} | "
        f"{customer['name']} | "
        f"{customer['email']} | "
        f"{customer['city']}"
    )
