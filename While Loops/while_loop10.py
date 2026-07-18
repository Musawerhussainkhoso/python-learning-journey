#Banking Transaction History
balance = 10000
transaction_number = 1

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Select an option: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            balance += amount
            print("Transaction", transaction_number, "completed.")
            print("Deposited:", amount)
            transaction_number += 1
        else:
            print("Invalid deposit amount.")

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > balance:
            print("Insufficient balance.")
        else:
            balance -= amount
            print("Transaction", transaction_number, "completed.")
            print("Withdrawn:", amount)
            transaction_number += 1

    elif choice == "3":
        print("Current balance:", balance)

    elif choice == "4":
        print("Banking session closed.")
        break

    else:
        print("Invalid option.")