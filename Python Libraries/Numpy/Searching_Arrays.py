import numpy as np 
#Question: Find where 50 exists.
import numpy as np

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

result = np.where(arr == 50)

print(result)

#Question: Find all values greater than 30.
arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

result = np.where(arr > 30)

print(result)
print(arr[result])

#Question: Find where 70 exists.
arr = np.array([
    [
        [10, 20],
        [30, 40]
    ],
    [
        [50, 60],
        [70, 80]
    ]
])
result = np.where(arr == 70)
print(result)

#Question: Find all values greater than 40.
arr = np.array([
    [
        [10, 20],
        [30, 40]
    ],
    [
        [50, 60],
        [70, 80]
    ]
])
result = np.where(arr > 40)
print(result)
print(arr[result])

'''
output of ques 04
50 → block 1, row 0, column 0
60 → block 1, row 0, column 1
70 → block 1, row 1, column 0
80 → block 1, row 1, column 1
'''
