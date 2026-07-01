import numpy as np 
'''
Question 1
Create a 2 × 2 × 3 NumPy array.

Access:

3
5
8
12
'''
arr = np.array([
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9],
        [10, 11, 12]
    ]
])

print("3:", arr[0,0,2])#layer,row,column
print("5:", arr[0,1,1])
print("8:", arr[1,0,1])
print("12:", arr[1,1,2])

'''
Question 2
Create a 2 × 3 × 2 NumPy array containing numbers 10 to 120 (difference of 10).

Access:

20
60
70
120
'''
arr = np.array([
    [
        [10, 20],
        [30, 40],
        [50, 60]
    ],
    [
        [70, 80],
        [90, 100],
        [110, 120]
    ]
])

print("20:", arr[0,0,1])
print("60:", arr[0,2,1])
print("70:", arr[1,0,0])
print("120:", arr[1,2,1])

'''
Question 3
Create a 3 × 2 × 2 NumPy array containing numbers 1 to 12.

Access:

1
6
9
12
'''
import numpy as np

arr = np.array([
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ],
    [
        [9, 10],
        [11, 12]
    ]
])

print("1:", arr[0,0,0])
print("6:", arr[1,0,1])
print("9:", arr[2,0,0])
print("12:", arr[2,1,1])

