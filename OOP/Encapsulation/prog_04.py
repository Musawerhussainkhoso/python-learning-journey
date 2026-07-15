#This program protects account balance and prevents direct invalid changes.
class BankAccount:
    def __init__(
        self,
        account_number: str,
        account_holder: str,
        opening_balance: float = 0.0
    ):
        if opening_balance < 0:
            raise ValueError(
                "Opening balance cannot be negative."
            )

        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__balance = opening_balance
        self.__transactions = []

    @property
    def account_number(self) -> str:
        return self.__account_number

    @property
    def account_holder(self) -> str:
        return self.__account_holder

    @property
    def balance(self) -> float:
        return self.__balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError(
                "Deposit amount must be greater than zero."
            )

        self.__balance += amount

        self.__transactions.append({
            "type": "Deposit",
            "amount": amount,
            "balance": self.__balance
        })

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError(
                "Withdrawal amount must be greater than zero."
            )

        if amount > self.__balance:
            raise ValueError("Insufficient account balance.")

        self.__balance -= amount

        self.__transactions.append({
            "type": "Withdrawal",
            "amount": amount,
            "balance": self.__balance
        })

    def get_transaction_history(self) -> list[dict]:
        return self.__transactions.copy()

    def display_account_summary(self) -> None:
        print("\nBANK ACCOUNT SUMMARY")
        print("=" * 55)
        print(f"Account Number : {self.__account_number}")
        print(f"Account Holder : {self.__account_holder}")
        print(f"Balance        : Rs. {self.__balance:,.2f}")

        print("\nTransaction History")

        if not self.__transactions:
            print("No transactions found.")
            return

        for transaction in self.__transactions:
            print(
                f"{transaction['type']:<12} "
                f"Rs. {transaction['amount']:>12,.2f} "
                f"Balance: Rs. {transaction['balance']:,.2f}"
            )


try:
    account = BankAccount(
        "PK-10004567",
        "Abdul Majid",
        100000
    )

    account.deposit(25000)
    account.withdraw(18000)
    account.deposit(12000)

    account.display_account_summary()

except ValueError as error:
    print(f"Banking error: {error}")