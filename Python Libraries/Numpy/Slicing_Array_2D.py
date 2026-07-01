# 1. Print the first 3 rows.
# 2. Print the last 2 rows.
# 3. Print the first 2 columns.
# 4. Print the last 3 columns.
import numpy as np

arr = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25]
])

print(arr[:3, :])

print(arr[3:, :])

print(arr[:, :2])

print(arr[:, 2:])

# Print:
# 1. The center 3×3 block.
# 2. The top-right 2×2 block.
# 3. The bottom-left 2×2 block.

arr = np.array([
    [10,20,30,40,50],
    [60,70,80,90,100],
    [110,120,130,140,150],
    [160,170,180,190,200],
    [210,220,230,240,250]
])

print(arr[1:4,1:4])

print(arr[:2,3:])

print(arr[3:,:2])

# Print:
# 1. Rows 1 to 3 and Columns 2 to 5.
# 2. First 3 columns of the last 2 rows.
# 3. Last 2 columns of the first 3 rows.
# 4. Only the second row.
arr = np.array([
    [5,10,15,20,25,30],
    [35,40,45,50,55,60],
    [65,70,75,80,85,90],
    [95,100,105,110,115,120]
])

print(arr[1:4,2:6])

print(arr[2:,:3])

print(arr[:3,4:])

print(arr[1,:])