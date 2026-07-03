import numpy as np 
#Program 1: Sort sales amounts in ascending and descending order
sales = np.array([45000, 12000, 78000, 23000, 56000])

ascending_sales = np.sort(sales)
descending_sales = np.sort(sales)[::-1]#:: slicing operator

print("Original Sales:", sales)
print("Ascending Sales:", ascending_sales)
print("Descending Sales:", descending_sales)

#Program 2: Sort student marks and find top 3 marks
marks = np.array([72, 88, 91, 65, 79, 95, 84])

sorted_marks = np.sort(marks)
top_3_marks = sorted_marks[-3:][::-1]

print("Original Marks:", marks)
print("Sorted Marks:", sorted_marks)
print("Top 3 Marks:", top_3_marks)

#Program 3: Sort each employee’s monthly sales row-wise
monthly_sales = np.array([
    [45000, 22000, 67000],
    [30000, 15000, 50000],
    [80000, 60000, 70000]
])

row_wise_sort = np.sort(monthly_sales, axis=1)

print("Original Monthly Sales:")
print(monthly_sales)

print("\nRow-wise Sorted Sales:")
print(row_wise_sort)

#Program 4: Sort product prices column-wise across branches
product_prices = np.array([
    [500, 1200, 300],
    [450, 1500, 250],
    [700, 1000, 400]
])

column_wise_sort = np.sort(product_prices, axis=0)

print("Original Product Prices:")
print(product_prices)

print("\nColumn-wise Sorted Prices:")
print(column_wise_sort)

#Program 6: Sort inventory quantity across warehouses
inventory = np.array([
    [
        [50, 20],
        [90, 40]
    ],
    [
        [30, 60],
        [70, 10]
    ],
    [
        [80, 25],
        [45, 100]
    ]
])

sorted_inventory = np.sort(inventory, axis=0)

print("Original Inventory Data:")
print(inventory)

print("\nInventory Sorted Across Warehouses:")
print(sorted_inventory)