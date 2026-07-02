import numpy as np 
'''A company stores the monthly sales of 12 months in a 1D array. 
Convert the data into 4 quarters, where each quarter contains 3 months.
'''
# Step 1: Create a 1D array
monthly_sales = np.array([
    1200, 1500, 1800,
    2000, 2200, 2500,
    2700, 3000, 3200,
    3500, 3800, 4000
])

print("Original Array:")
print(monthly_sales)

# Step 2: Reshape into 4 rows and 3 columns
quarterly_sales = monthly_sales.reshape(4, 3)

print("\nReshaped Array:")
print(quarterly_sales)

print("\nShape:", quarterly_sales.shape)

'''
A university stores marks of 4 students in 3 subjects.
Convert the array into 2 classes, where each class contains 2 students.
'''
# Step 1: Create a 2D array
marks = np.array([
    [85, 90, 88],
    [78, 82, 80],
    [92, 95, 91],
    [70, 75, 73]
])

print("Original Array:")
print(marks)

# Step 2: Reshape into 3D
class_marks = marks.reshape(2, 2, 3)

print("\nReshaped Array:")
print(class_marks)

print("\nShape:", class_marks.shape)

'''
A security system stores pixel values from 2 cameras. 
Each camera captures 2 rows and 3 columns. Convert the data into a 2D array.
'''
import numpy as np

# Step 1: Create a 3D array
camera_data = np.array([
    [
        [10, 20, 30],
        [40, 50, 60]
    ],
    [
        [70, 80, 90],
        [100, 110, 120]
    ]
])

print("Original Array:")
print(camera_data)

# Step 2: Reshape into 2D
camera_matrix = camera_data.reshape(4, 3)

print("\nReshaped Array:")
print(camera_matrix)

print("\nShape:", camera_matrix.shape)


