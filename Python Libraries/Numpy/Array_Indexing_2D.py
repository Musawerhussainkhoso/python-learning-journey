import numpy as np
#Create a 4 × 4 NumPy array containing numbers
#10 to 160 (difference of 10) and access 40, 90, 110, and 160.
arr = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120],
    [130, 140, 150, 160]
])
print("40:", arr[0,3])
print("90:", arr[2,0])
print("110:", arr[2,2])
print("160:", arr[3,3])

