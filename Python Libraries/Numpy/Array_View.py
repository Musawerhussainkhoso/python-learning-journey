'''
Employee Attendance View

A company's HR department wants to create a view of the employee attendance records. Any changes 
made to the original attendance array should automatically appear in the view.

Task 01
Create the following NumPy array:
[1, 1, 0, 1, 0, 1]

(1 = Present, 0 = Absent)

Create a view called attendance_view.
Update:
First employee → 0
Last employee → 0
Print:
Original attendance array
Attendance view
Check whether both arrays are equal.
Print attendance_view.base.
'''
import numpy as np

# Step 1: Create the original attendance array
attendance = np.array([1, 1, 0, 1, 0, 1])

# Step 2: Create a view
attendance_view = attendance.view()

# Step 3: Update the original array
attendance[0] = 0
attendance[-1] = 0

# Step 4: Print both arrays
print("Original Attendance:", attendance)
print("Attendance View:", attendance_view)

# Step 5: Check whether both arrays are equal
print("Are both arrays equal?", np.array_equal(attendance, attendance_view))

# Step 6: Print the parent array
print("attendance_view.base:", attendance_view.base)

'''
Product Prices View

An e-commerce company stores product prices in a NumPy array. The finance team creates a view to 
monitor the prices.

Task 02
Create the following NumPy array:
[2500, 1800, 3200, 1500, 4000]
Create a view named price_view.
Update the view:
Second product price → 2000
Fourth product price → 1700
Print:
Original price array
Price view
Check whether both arrays are equal.
Print price_view.base.
'''


# Step 1: Create the original price array
prices = np.array([2500, 1800, 3200, 1500, 4000])

# Step 2: Create a view
price_view = prices.view()

# Step 3: Update the view
price_view[1] = 2000
price_view[3] = 1700

# Step 4: Print both arrays
print("Original Prices:", prices)
print("Price View:", price_view)

# Step 5: Check whether both arrays are equal
print("Are both arrays equal?", np.array_equal(prices, price_view))

# Step 6: Print the parent array
print("price_view.base:", price_view.base)

