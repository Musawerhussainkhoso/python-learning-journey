#This program cleans names and emails, removes duplicate customers, and rejects invalid records.
def clean_customer_data(
    raw_customers: list[dict]
) -> tuple[list[dict], list[dict]]:

    cleaned_customers = []
    rejected_customers = []
    registered_emails = set()

    for customer in raw_customers:
        name = customer["name"].strip().title()
        email = customer["email"].strip().lower()
        city = customer["city"].strip().title()

        if not name or not email:
            customer["rejection_reason"] = "Missing name or email"
            rejected_customers.append(customer)
            continue

        if "@" not in email or "." not in email:
            customer["rejection_reason"] = "Invalid email address"
            rejected_customers.append(customer)
            continue

        if email in registered_emails:
            customer["rejection_reason"] = "Duplicate email address"
            rejected_customers.append(customer)
            continue

        registered_emails.add(email)

        cleaned_customers.append({
            "customer_id": customer["customer_id"],
            "name": name,
            "email": email,
            "city": city
        })

    return cleaned_customers, rejected_customers


raw_customers = [
    {
        "customer_id": 101,
        "name": "  ali khan ",
        "email": "ALI@GMAIL.COM ",
        "city": "karachi"
    },
    {
        "customer_id": 102,
        "name": "sara ahmed",
        "email": "sara@gmail.com",
        "city": " lahore "
    },
    {
        "customer_id": 103,
        "name": "hamza ali",
        "email": "invalid-email",
        "city": "hyderabad"
    },
    {
        "customer_id": 104,
        "name": "Ali Duplicate",
        "email": "ali@gmail.com",
        "city": "islamabad"
    }
]

cleaned, rejected = clean_customer_data(raw_customers)

print("\nCLEANED CUSTOMER DATA")
print("=" * 60)

for customer in cleaned:
    print(customer)

print("\nREJECTED CUSTOMER DATA")
print("=" * 60)

for customer in rejected:
    print(
        f"Customer ID: {customer['customer_id']}, "
        f"Reason: {customer['rejection_reason']}"
    )