'''
This program processes deposit and 
withdrawal transactions and creates a complete account summary.
'''
from typing import Dict, List
Account = Dict[str, object]
Transaction = Dict[str, object]
def process_transaction(
    account: Account,
    transaction: Transaction
) -> bool:

    transaction_type = str(transaction["type"]).lower()
    amount = float(transaction["amount"])
    current_balance = float(account["balance"])

    if amount <= 0:
        print("Transaction amount must be greater than zero.")
        return False

    if transaction_type == "deposit":
        account["balance"] = current_balance + amount
        transaction["status"] = "Completed"

    elif transaction_type == "withdrawal":
        if amount > current_balance:
            transaction["status"] = "Rejected"
            transaction["reason"] = "Insufficient balance"
            return False

        account["balance"] = current_balance - amount
        transaction["status"] = "Completed"

    else:
        transaction["status"] = "Rejected"
        transaction["reason"] = "Invalid transaction type"
        return False

    account["transactions"].append(transaction)

    return True


def generate_account_statement(account: Account) -> None:
    print("\nBANK ACCOUNT STATEMENT")
    print("=" * 70)

    print(f"Account Number : {account['account_number']}")
    print(f"Account Holder : {account['account_holder']}")
    print(f"Account Type   : {account['account_type']}")

    print("\nTRANSACTION HISTORY")
    print("-" * 70)

    transactions = account["transactions"]

    if not transactions:
        print("No completed transactions found.")
    else:
        for transaction in transactions:
            print(f"ID     : {transaction['transaction_id']}")
            print(f"Type   : {transaction['type'].title()}")
            print(f"Amount : Rs. {transaction['amount']:,.2f}")
            print(f"Status : {transaction['status']}")
            print("-" * 70)

    print(
        f"Current Balance: "
        f"Rs. {float(account['balance']):,.2f}"
    )


bank_account = {
    "account_number": "PK-10004567",
    "account_holder": "Abdul Majid",
    "account_type": "Savings",
    "balance": 125000.00,
    "transactions": []
}


pending_transactions: List[Transaction] = [
    {
        "transaction_id": "TXN-001",
        "type": "deposit",
        "amount": 30000.00
    },
    {
        "transaction_id": "TXN-002",
        "type": "withdrawal",
        "amount": 25000.00
    },
    {
        "transaction_id": "TXN-003",
        "type": "withdrawal",
        "amount": 200000.00
    },
    {
        "transaction_id": "TXN-004",
        "type": "deposit",
        "amount": 15000.00
    }
]


for transaction in pending_transactions:
    successful = process_transaction(
        bank_account,
        transaction
    )

    if not successful:
        print(
            f"Transaction {transaction['transaction_id']} "
            f"failed: {transaction.get('reason')}"
        )
generate_account_statement(bank_account)
