import numpy as np
'''
np.split()       → equal parts required
np.array_split() → equal parts not required
'''
#1. Splitting 1D Array Using np.split()
arr = np.array([10, 20, 30, 40, 50, 60])
result = np.split(arr, 3)
print(result)

#2. Splitting 1D Array Using np.array_split()
arr = np.array([10, 20, 30, 40, 50])
result = np.array_split(arr, 3)
print(result)

#3. Splitting 2D Array with axis=0
import numpy as np

arr = np.array([
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8]
])

result = np.split(arr, 2, axis=0)

print(result)
