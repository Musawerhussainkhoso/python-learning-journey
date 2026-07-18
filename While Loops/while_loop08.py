#Inventory Stock Management
stock = 100

while stock > 0:
    print("\nAvailable stock:", stock)

    quantity = int(input("Enter order quantity or 0 to stop: "))

    if quantity == 0:
        print("Order processing stopped.")
        break

    if quantity < 0:
        print("Quantity cannot be negative.")

    elif quantity > stock:
        print("Not enough stock available.")

    else:
        stock -= quantity
        print("Order completed.")
        print("Remaining stock:", stock)

if stock == 0:
    print("The product is out of stock.")