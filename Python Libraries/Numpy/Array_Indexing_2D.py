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

'''
Create a 3 × 5 NumPy array containing numbers 5 to 75 (difference of 5).

Access:

15
35
55
75
'''
arr = np.array([
    [5, 10, 15, 20, 25],
    [30, 35, 40, 45, 50],
    [55, 60, 65, 70, 75]
])

print("15:", arr[0,2])
print("35:", arr[1,1])
print("55:", arr[2,0])
print("75:", arr[2,4])

'''
Create a 5 × 4 NumPy array containing numbers 1 to 20.

Access:

2
8
13
20
'''
arr = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
    [17, 18, 19, 20]
])

print("2:", arr[0,1])
print("8:", arr[1,3])
print("13:", arr[3,0])
print("20:", arr[4,3])

