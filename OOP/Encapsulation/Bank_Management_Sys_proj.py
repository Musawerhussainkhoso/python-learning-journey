#banking management system
from abc import ABC, abstractmethod
from datetime import datetime


# ============================================================
# ABSTRACT BASE CLASS
# ============================================================

class BankAccount(ABC):

    def __init__(
        self,
        account_number: str,
        account_holder: str,
        initial_balance: float = 0.0
    ):
        # Encapsulation: private attributes
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__balance = initial_balance
        self.__created_at = datetime.now()
        self.__transaction_history = []

    # Getter methods
    def get_account_number(self) -> str:
        return self.__account_number

    def get_account_holder(self) -> str:
        return self.__account_holder

    def get_balance(self) -> float:
        return self.__balance

    def get_created_at(self) -> datetime:
        return self.__created_at

    def get_transaction_history(self) -> list:
        return self.__transaction_history.copy()

    # Setter method
    def set_account_holder(self, new_name: str) -> None:
        if not new_name.strip():
            raise ValueError("Account holder name cannot be empty.")

        self.__account_holder = new_name

    # Protected methods
    def _add_balance(self, amount: float) -> None:
        self.__balance += amount

    def _subtract_balance(self, amount: float) -> None:
        self.__balance -= amount

    def _add_transaction(self, description: str) -> None:
        transaction = {
            "date": datetime.now(),
            "description": description,
            "balance": self.__balance
        }

        self.__transaction_history.append(transaction)

    def _validate_amount(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

    def display_account_information(self) -> None:
        print("\n" + "=" * 55)
        print("BANK ACCOUNT INFORMATION")
        print("=" * 55)
        print(f"Account Number : {self.__account_number}")
        print(f"Account Holder : {self.__account_holder}")
        print(f"Account Type   : {self.get_account_type()}")
        print(f"Balance        : Rs. {self.__balance:,.2f}")
        print(
            f"Created At     : "
            f"{self.__created_at.strftime('%d-%m-%Y %I:%M %p')}"
        )
        print("=" * 55)

    def display_transaction_history(self) -> None:
        print("\n" + "=" * 70)
        print(f"TRANSACTION HISTORY - {self.__account_number}")
        print("=" * 70)

        if not self.__transaction_history:
            print("No transactions found.")
            return

        for index, transaction in enumerate(
            self.__transaction_history,
            start=1
        ):
            print(f"\nTransaction {index}")
            print(
                "Date        :",
                transaction["date"].strftime("%d-%m-%Y %I:%M %p")
            )
            print("Description :", transaction["description"])
            print(f"Balance     : Rs. {transaction['balance']:,.2f}")

    # Abstraction
    @abstractmethod
    def deposit(self, amount: float) -> None:
        pass

    @abstractmethod
    def withdraw(self, amount: float) -> None:
        pass

    @abstractmethod
    def calculate_monthly_return(self) -> float:
        pass

    @abstractmethod
    def get_account_type(self) -> str:
        pass


# ============================================================
# SAVINGS ACCOUNT
# ============================================================

class SavingsAccount(BankAccount):

    def __init__(
        self,
        account_number: str,
        account_holder: str,
        initial_balance: float,
        interest_rate: float = 0.05
    ):
        super().__init__(
            account_number,
            account_holder,
            initial_balance
        )

        # Encapsulation
        self.__interest_rate = interest_rate
        self.__minimum_balance = 1000

    def get_interest_rate(self) -> float:
        return self.__interest_rate

    def set_interest_rate(self, interest_rate: float) -> None:
        if interest_rate < 0:
            raise ValueError("Interest rate cannot be negative.")

        self.__interest_rate = interest_rate

    def deposit(self, amount: float) -> None:
        self._validate_amount(amount)
        self._add_balance(amount)

        self._add_transaction(
            f"Savings account deposit of Rs. {amount:,.2f}"
        )

        print(
            f"Rs. {amount:,.2f} deposited successfully "
            "into Savings Account."
        )

    def withdraw(self, amount: float) -> None:
        self._validate_amount(amount)

        remaining_balance = self.get_balance() - amount

        if amount > self.get_balance():
            raise ValueError("Insufficient balance.")

        if remaining_balance < self.__minimum_balance:
            raise ValueError(
                f"You must maintain a minimum balance of "
                f"Rs. {self.__minimum_balance:,.2f}."
            )

        self._subtract_balance(amount)

        self._add_transaction(
            f"Savings account withdrawal of Rs. {amount:,.2f}"
        )

        print(
            f"Rs. {amount:,.2f} withdrawn successfully "
            "from Savings Account."
        )

    def calculate_monthly_return(self) -> float:
        monthly_interest_rate = self.__interest_rate / 12
        return self.get_balance() * monthly_interest_rate

    def add_monthly_interest(self) -> None:
        interest = self.calculate_monthly_return()
        self._add_balance(interest)

        self._add_transaction(
            f"Monthly interest added: Rs. {interest:,.2f}"
        )

        print(f"Monthly interest of Rs. {interest:,.2f} added.")

    def get_account_type(self) -> str:
        return "Savings Account"


# ============================================================
# CURRENT ACCOUNT
# ============================================================

class CurrentAccount(BankAccount):

    def __init__(
        self,
        account_number: str,
        account_holder: str,
        initial_balance: float,
        overdraft_limit: float = 50000
    ):
        super().__init__(
            account_number,
            account_holder,
            initial_balance
        )

        # Encapsulation
        self.__overdraft_limit = overdraft_limit
        self.__monthly_service_charge = 500

    def get_overdraft_limit(self) -> float:
        return self.__overdraft_limit

    def set_overdraft_limit(self, new_limit: float) -> None:
        if new_limit < 0:
            raise ValueError("Overdraft limit cannot be negative.")

        self.__overdraft_limit = new_limit

    def deposit(self, amount: float) -> None:
        self._validate_amount(amount)
        self._add_balance(amount)

        self._add_transaction(
            f"Current account deposit of Rs. {amount:,.2f}"
        )

        print(
            f"Rs. {amount:,.2f} deposited successfully "
            "into Current Account."
        )

    def withdraw(self, amount: float) -> None:
        self._validate_amount(amount)

        available_amount = (
            self.get_balance() + self.__overdraft_limit
        )

        if amount > available_amount:
            raise ValueError(
                "Withdrawal amount exceeds balance and overdraft limit."
            )

        self._subtract_balance(amount)

        self._add_transaction(
            f"Current account withdrawal of Rs. {amount:,.2f}"
        )

        print(
            f"Rs. {amount:,.2f} withdrawn successfully "
            "from Current Account."
        )

    def calculate_monthly_return(self) -> float:
        return -self.__monthly_service_charge

    def deduct_monthly_service_charge(self) -> None:
        charge = self.__monthly_service_charge
        self._subtract_balance(charge)

        self._add_transaction(
            f"Monthly service charge deducted: Rs. {charge:,.2f}"
        )

        print(
            f"Monthly service charge of Rs. {charge:,.2f} deducted."
        )

    def get_account_type(self) -> str:
        return "Current Account"


# ============================================================
# FIXED DEPOSIT ACCOUNT
# ============================================================

class FixedDepositAccount(BankAccount):

    def __init__(
        self,
        account_number: str,
        account_holder: str,
        initial_balance: float,
        annual_interest_rate: float = 0.10,
        duration_months: int = 12
    ):
        super().__init__(
            account_number,
            account_holder,
            initial_balance
        )

        self.__annual_interest_rate = annual_interest_rate
        self.__duration_months = duration_months
        self.__is_matured = False

    def deposit(self, amount: float) -> None:
        raise ValueError(
            "Additional deposits are not allowed in a Fixed Deposit Account."
        )

    def withdraw(self, amount: float) -> None:
        if not self.__is_matured:
            raise ValueError(
                "Withdrawal is not allowed before account maturity."
            )

        self._validate_amount(amount)

        if amount > self.get_balance():
            raise ValueError("Insufficient balance.")

        self._subtract_balance(amount)

        self._add_transaction(
            f"Fixed deposit withdrawal of Rs. {amount:,.2f}"
        )

        print(
            f"Rs. {amount:,.2f} withdrawn from Fixed Deposit Account."
        )

    def calculate_monthly_return(self) -> float:
        monthly_rate = self.__annual_interest_rate / 12
        return self.get_balance() * monthly_rate

    def calculate_maturity_amount(self) -> float:
        monthly_return = self.calculate_monthly_return()

        total_interest = (
            monthly_return * self.__duration_months
        )

        return self.get_balance() + total_interest

    def mark_as_matured(self) -> None:
        maturity_amount = self.calculate_maturity_amount()
        interest = maturity_amount - self.get_balance()

        self._add_balance(interest)
        self.__is_matured = True

        self._add_transaction(
            f"Fixed deposit matured. Interest added: "
            f"Rs. {interest:,.2f}"
        )

        print("Fixed Deposit Account has matured.")
        print(f"Interest added: Rs. {interest:,.2f}")

    def get_account_type(self) -> str:
        return "Fixed Deposit Account"


# ============================================================
# POLYMORPHIC FUNCTION
# ============================================================

def process_account(account: BankAccount) -> None:
    print("\nProcessing account...")
    print(f"Account Type: {account.get_account_type()}")
    print(
        f"Monthly Return: "
        f"Rs. {account.calculate_monthly_return():,.2f}"
    )
    account.display_account_information()


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():

    savings_account = SavingsAccount(
        account_number="SA-1001",
        account_holder="Ali Khan",
        initial_balance=100000,
        interest_rate=0.06
    )

    current_account = CurrentAccount(
        account_number="CA-2001",
        account_holder="Sara Ahmed",
        initial_balance=50000,
        overdraft_limit=30000
    )

    fixed_account = FixedDepositAccount(
        account_number="FD-3001",
        account_holder="Bilal Hussain",
        initial_balance=200000,
        annual_interest_rate=0.12,
        duration_months=12
    )

    try:
        savings_account.deposit(20000)
        savings_account.withdraw(10000)
        savings_account.add_monthly_interest()

        current_account.deposit(15000)
        current_account.withdraw(70000)
        current_account.deduct_monthly_service_charge()

        fixed_account.mark_as_matured()
        fixed_account.withdraw(50000)

    except ValueError as error:
        print("Transaction Error:", error)

    # Polymorphism
    accounts = [
        savings_account,
        current_account,
        fixed_account
    ]

    for account in accounts:
        process_account(account)

    savings_account.display_transaction_history()
    current_account.display_transaction_history()
    fixed_account.display_transaction_history()


if __name__ == "__main__":
    main()