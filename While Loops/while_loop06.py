#ATM Withdrawal System
balance = 50000

while True:
    print("\nCurrent Balance:", balance)
    amount = int(input("Enter withdrawal amount or 0 to exit: "))

    if amount == 0:
        print("Transaction ended.")
        break

    if amount < 0:
        print("Invalid amount.")

    elif amount > balance:
        print("Insufficient balance.")

    elif amount % 500 != 0:
        print("Amount must be a multiple of 500.")

    else:
        balance -= amount
        print("Withdrawal successful.")
        print("Remaining balance:", balance)