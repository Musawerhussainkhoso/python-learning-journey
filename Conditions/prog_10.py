#This program compares actual expenses with category budgets.
def generate_budget_report(
    budgets: dict[str, float],
    expenses: list[dict]
) -> None:

    category_expenses = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        category_expenses[category] = (
            category_expenses.get(category, 0) + amount
        )

    print("\nMONTHLY BUDGET REPORT")
    print("=" * 75)

    total_budget = 0.0
    total_expense = 0.0

    for category, budget in budgets.items():
        spent = category_expenses.get(category, 0)
        remaining = budget - spent

        total_budget += budget
        total_expense += spent

        if remaining < 0:
            status = f"Over budget by Rs. {abs(remaining):,.2f}"
        else:
            status = f"Remaining Rs. {remaining:,.2f}"

        print(f"Category : {category}")
        print(f"Budget   : Rs. {budget:,.2f}")
        print(f"Spent    : Rs. {spent:,.2f}")
        print(f"Status   : {status}")
        print("-" * 75)

    total_remaining = total_budget - total_expense

    print(f"Total budget  : Rs. {total_budget:,.2f}")
    print(f"Total expense : Rs. {total_expense:,.2f}")
    print(f"Net remaining : Rs. {total_remaining:,.2f}")


budgets = {
    "Rent": 50000,
    "Food": 30000,
    "Transport": 15000,
    "Utilities": 12000,
    "Education": 20000
}

expenses = [
    {"category": "Rent", "amount": 50000},
    {"category": "Food", "amount": 8500},
    {"category": "Food", "amount": 12000},
    {"category": "Food", "amount": 11000},
    {"category": "Transport", "amount": 9000},
    {"category": "Utilities", "amount": 14500},
    {"category": "Education", "amount": 15000}
]

generate_budget_report(budgets, expenses)