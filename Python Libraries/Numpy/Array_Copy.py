'''
An inventory system stores the stock quantities of products.

Task
Create the following NumPy array:
[120, 85, 60, 150, 95, 40]
Create a copy called stock_backup.

Update:
First product stock → 100
Last product stock → 70

Print:
Original stock array
Backup stock array
Check whether the backup changed.
Print stock_backup.base
'''
import numpy as np

# Step 1: Create the original stock array
stock = np.array([120, 85, 60, 150, 95, 40])

# Step 2: Create a backup using copy()
stock_backup = stock.copy()

# Step 3: Update the original array
stock[0] = 100
stock[-1] = 70

# Step 4: Print both arrays
print("Original Stock:", stock)
print("Backup Stock:", stock_backup)

# Step 5: Check whether the backup changed
print("Did the backup change?")
print(np.array_equal(stock, stock_backup))

# Step 6: Print the base of the backup array
print("stock_backup.base:", stock_backup.base)#.base tells us whether an array has a parent array. If the array is created with copy(), it gets new memory, so it has no parent and .base returns None. If it is created with view(), it shares the original array's memory, so .base returns the parent array.

