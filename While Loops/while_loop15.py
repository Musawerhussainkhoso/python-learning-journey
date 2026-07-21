#ATM System with PIN Attempts
print("=" * 45)
print("PYTHON ATM MANAGEMENT SYSTEM")
print("=" * 45)

correct_pin = "7860"
account_balance = 50000

pin_attempts = 0
maximum_attempts = 3
access_granted = False

while pin_attempts < maximum_attempts:
    entered_pin = input("Enter your four-digit PIN: ")

    if entered_pin == correct_pin:
        access_granted = True
        print("PIN accepted. Access granted.")
        break

    pin_attempts += 1
    remaining_attempts = maximum_attempts - pin_attempts

    print("Incorrect PIN.")

    if remaining_attempts > 0:
        print("Remaining Attempts:", remaining_attempts)

if access_granted:
    total_withdrawn = 0
    total_deposited = 0
    transaction_count = 0

    choice = 0

    while choice != 5:
        print("\n" + "-" * 35)
        print("ATM MENU")
        print("-" * 35)
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. View Transaction Summary")
        print("5. Exit")

        choice = int(input("Select an option: "))

        if choice == 1:
            print("Available Balance:", account_balance)

        elif choice == 2:
            withdrawal_amount = float(
                input("Enter withdrawal amount: ")
            )

            while withdrawal_amount <= 0:
                print("Amount must be greater than zero.")
                withdrawal_amount = float(
                    input("Enter valid withdrawal amount: ")
                )

            if withdrawal_amount > account_balance:
                print("Insufficient account balance.")

            elif withdrawal_amount % 500 != 0:
                print("Amount must be a multiple of 500.")

            else:
                account_balance -= withdrawal_amount
                total_withdrawn += withdrawal_amount
                transaction_count += 1

                print("Please collect your cash.")
                print("Remaining Balance:", account_balance)

        elif choice == 3:
            deposit_amount = float(input("Enter deposit amount: "))

            while deposit_amount <= 0:
                print("Deposit amount must be greater than zero.")
                deposit_amount = float(
                    input("Enter valid deposit amount: ")
                )

            account_balance += deposit_amount
            total_deposited += deposit_amount
            transaction_count += 1

            print("Amount deposited successfully.")
            print("Updated Balance:", account_balance)

        elif choice == 4:
            print("\nTRANSACTION SUMMARY")
            print("-" * 35)
            print("Total Deposited   :", total_deposited)
            print("Total Withdrawn   :", total_withdrawn)
            print("Transaction Count :", transaction_count)
            print("Current Balance   :", account_balance)

        elif choice == 5:
            print("Thank you for using the ATM.")

        else:
            print("Invalid option. Please try again.")

else:
    print("\nYour account has been temporarily blocked.")
    print("Reason: Three incorrect PIN attempts.")