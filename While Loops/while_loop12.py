#Banking System with Menu
print("=" * 45)
print("WELCOME TO PYTHON BANKING SYSTEM")
print("=" * 45)

account_holder = input("Enter account holder name: ").strip()

while account_holder == "":
    print("Name cannot be empty.")
    account_holder = input("Enter account holder name: ").strip()

balance = float(input("Enter initial account balance: "))

while balance < 0:
    print("Initial balance cannot be negative.")
    balance = float(input("Enter valid initial balance: "))

total_deposited = 0
total_withdrawn = 0
transaction_count = 0

choice = 0

while choice != 4:
    print("\n" + "-" * 35)
    print("BANKING MENU")
    print("-" * 35)
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Account Details")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        deposit_amount = float(input("Enter deposit amount: "))

        while deposit_amount <= 0:
            print("Deposit amount must be greater than zero.")
            deposit_amount = float(
                input("Enter valid deposit amount: ")
            )

        balance += deposit_amount
        total_deposited += deposit_amount
        transaction_count += 1

        print("Deposit successful.")
        print("Current Balance:", balance)

    elif choice == 2:
        withdrawal_amount = float(input("Enter withdrawal amount: "))

        while withdrawal_amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            withdrawal_amount = float(
                input("Enter valid withdrawal amount: ")
            )

        if withdrawal_amount <= balance:
            balance -= withdrawal_amount
            total_withdrawn += withdrawal_amount
            transaction_count += 1

            print("Withdrawal successful.")
            print("Remaining Balance:", balance)
        else:
            print("Insufficient account balance.")

    elif choice == 3:
        print("\nACCOUNT DETAILS")
        print("-" * 35)
        print("Account Holder  :", account_holder)
        print("Current Balance :", balance)
        print("Total Deposited :", total_deposited)
        print("Total Withdrawn :", total_withdrawn)
        print("Transactions    :", transaction_count)

    elif choice == 4:
        print("\nThank you for using the banking system.")

    else:
        print("Invalid choice. Please select between 1 and 4.")

print("\nFINAL ACCOUNT SUMMARY")
print("-" * 35)
print("Account Holder    :", account_holder)
print("Closing Balance   :", balance)
print("Total Deposited   :", total_deposited)
print("Total Withdrawn   :", total_withdrawn)
print("Total Transactions:", transaction_count)