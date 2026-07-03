import numpy as np 
#A company has daily sales amounts. Filter only those sales which are greater than 50000.
sales = np.array([25000, 60000, 45000, 90000, 12000, 75000])

high_sales = sales[sales > 50000]

print("Original Sales:", sales)
print("High Sales:", high_sales)

#A teacher wants to filter only passing marks. Passing marks are 50 or above.
marks = np.array([35, 82, 49, 67, 90, 44, 55])

passing_marks = marks[marks >= 50]

print("Original Marks:", marks)
print("Passing Marks:", passing_marks)

#A company has product prices from different branches. Filter only prices greater than 1000.
prices = np.array([
    [500, 1200, 800],
    [1500, 700, 2000],
    [300, 1800, 900]
])

expensive_prices = prices[prices > 1000]

print("Original Prices:")
print(prices)

print("Expensive Prices:")
print(expensive_prices)

#Filter only those sales which are greater than 20000 and less than 70000.

sales = np.array([
    [15000, 45000, 90000],
    [30000, 65000, 12000],
    [80000, 25000, 50000]
])

filtered_sales = sales[(sales > 20000) & (sales < 70000)]

print("Original Sales:")
print(sales)

print("Sales Between 20000 and 70000:")
print(filtered_sales)

#A company has inventory data for multiple warehouses. Filter only quantities greater than 50.
inventory = np.array([
    [
        [20, 60, 35],
        [80, 45, 90]
    ],
    [
        [55, 30, 75],
        [25, 100, 40]
    ]
])

high_inventory = inventory[inventory > 50]

print("Original Inventory:")
print(inventory)

print("High Inventory Quantities:")
print(high_inventory)

#A factory has machine temperature readings from multiple sections. Filter only abnormal temperatures.
# Temperature above 75 is abnormal.
temperatures = np.array([
    [
        [65, 70, 80],
        [72, 60, 90]
    ],
    [
        [55, 78, 68],
        [85, 74, 95]
    ]
])

abnormal_temperatures = temperatures[temperatures > 75]

print("Original Temperatures:")
print(temperatures)

print("Abnormal Temperatures:")
print(abnormal_temperatures)