#Inventory Management System
print("=" * 50)
print("INVENTORY MANAGEMENT SYSTEM")
print("=" * 50)

product_name = input("Enter product name: ").strip()

while product_name == "":
    print("Product name cannot be empty.")
    product_name = input("Enter product name again: ").strip()

stock_quantity = int(input("Enter opening stock quantity: "))

while stock_quantity < 0:
    print("Stock quantity cannot be negative.")
    stock_quantity = int(input("Enter valid stock quantity: "))

price_per_unit = float(input("Enter price per unit: "))

while price_per_unit <= 0:
    print("Price must be greater than zero.")
    price_per_unit = float(input("Enter valid price per unit: "))

total_units_added = 0
total_units_sold = 0
total_sales = 0

choice = 0

while choice != 5:
    print("\n" + "-" * 40)
    print("INVENTORY MENU")
    print("-" * 40)
    print("1. Add Stock")
    print("2. Sell Product")
    print("3. View Stock")
    print("4. View Sales Report")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        added_quantity = int(input("Enter quantity to add: "))

        while added_quantity <= 0:
            print("Quantity must be greater than zero.")
            added_quantity = int(
                input("Enter valid quantity: ")
            )

        stock_quantity += added_quantity
        total_units_added += added_quantity

        print("Stock added successfully.")
        print("Updated Stock:", stock_quantity)

    elif choice == 2:
        sold_quantity = int(input("Enter quantity to sell: "))

        while sold_quantity <= 0:
            print("Quantity must be greater than zero.")
            sold_quantity = int(
                input("Enter valid quantity: ")
            )

        if sold_quantity <= stock_quantity:
            sale_amount = sold_quantity * price_per_unit

            stock_quantity -= sold_quantity
            total_units_sold += sold_quantity
            total_sales += sale_amount

            print("Sale completed successfully.")
            print("Sale Amount    :", sale_amount)
            print("Remaining Stock:", stock_quantity)
        else:
            print("Not enough stock available.")
            print("Available Stock:", stock_quantity)

    elif choice == 3:
        stock_value = stock_quantity * price_per_unit

        print("\nCURRENT STOCK DETAILS")
        print("-" * 35)
        print("Product Name   :", product_name)
        print("Available Units:", stock_quantity)
        print("Price Per Unit :", price_per_unit)
        print("Stock Value    :", stock_value)

    elif choice == 4:
        print("\nSALES REPORT")
        print("-" * 35)
        print("Product Name      :", product_name)
        print("Units Added       :", total_units_added)
        print("Units Sold        :", total_units_sold)
        print("Remaining Units   :", stock_quantity)
        print("Total Sales Amount:", total_sales)

    elif choice == 5:
        print("Inventory system closed successfully.")

    else:
        print("Invalid menu choice.")

print("\nFINAL INVENTORY SUMMARY")
print("-" * 40)
print("Product Name      :", product_name)
print("Remaining Stock   :", stock_quantity)
print("Total Units Sold  :", total_units_sold)
print("Total Sales       :", total_sales)