#6. Analyse Banking Transactions
def process_transactions(
    opening_balance: float,
    transactions: list[tuple[str, str, str, float]]
) -> tuple[float, list[tuple[str, str]]]:
    """
    Process bank transactions and return the final balance
    with rejected transactions.
    """

    current_balance = opening_balance
    rejected_transactions = []

    total_deposits = 0.0
    total_withdrawals = 0.0

    for transaction in transactions:
        transaction_id, account_number, transaction_type, amount = (
            transaction
        )

        if amount <= 0:
            rejected_transactions.append(
                (
                    transaction_id,
                    "Amount must be greater than zero"
                )
            )
            continue

        if transaction_type.lower() == "deposit":
            current_balance += amount
            total_deposits += amount

        elif transaction_type.lower() == "withdrawal":
            if amount > current_balance:
                rejected_transactions.append(
                    (
                        transaction_id,
                        "Insufficient balance"
                    )
                )
                continue

            current_balance -= amount
            total_withdrawals += amount

        else:
            rejected_transactions.append(
                (
                    transaction_id,
                    "Invalid transaction type"
                )
            )

    print("BANK TRANSACTION SUMMARY")
    print("=" * 60)
    print(f"Opening balance   : Rs. {opening_balance:,.2f}")
    print(f"Total deposits    : Rs. {total_deposits:,.2f}")
    print(f"Total withdrawals : Rs. {total_withdrawals:,.2f}")
    print(f"Closing balance   : Rs. {current_balance:,.2f}")

    return current_balance, rejected_transactions


transactions = [
    ("TXN-101", "ACC-5001", "Deposit", 50000),
    ("TXN-102", "ACC-5001", "Withdrawal", 25000),
    ("TXN-103", "ACC-5001", "Withdrawal", 200000),
    ("TXN-104", "ACC-5001", "Deposit", 15000),
    ("TXN-105", "ACC-5001", "Transfer", 10000),
    ("TXN-106", "ACC-5001", "Withdrawal", -5000)
]

final_balance, rejected = process_transactions(
    opening_balance=100000,
    transactions=transactions
)
print("\nREJECTED TRANSACTIONS")
print("-" * 60)
for transaction_id, reason in rejected:
    print(f"{transaction_id}: {reason}")