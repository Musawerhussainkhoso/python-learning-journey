import numpy as np 

#Program 1: 1D Array with axis=0 (axis = 0 means column wise)
#axis=1 does not exist in 1D, so it gives error.
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
result = np.concatenate((arr1, arr2), axis=0)
print(result)

#Program 2: 1D Array with axis=1
try:
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    result = np.concatenate((arr1, arr2), axis=1)
    print(result)
except Exception:
    print("axis 1 shows error in 1D arrays")
    
#Program 3: 2D Array with axis=0
arr1 = np.array([
    [1, 2],
    [3, 4]
])

arr2 = np.array([
    [5, 6],
    [7, 8]
])
result = np.concatenate((arr1, arr2), axis=0)
print(result)    

#Program 4: 2D Array with axis=1
arr1 = np.array([
    [1, 2],
    [3, 4]
])

arr2 = np.array([
    [5, 6],
    [7, 8]
])
result = np.concatenate((arr1, arr2), axis=1)
print(result)

#Program 5: 3D Array with axis=0
arr1 = np.array([
    [
        [1, 2],
        [3, 4]
    ]
])

arr2 = np.array([
    [
        [5, 6],
        [7, 8]
    ]
])
result = np.concatenate((arr1, arr2), axis=0)
print(result)
print(result.shape)

#Program 6: 3D Array with axis=1
arr1 = np.array([
    [
        [1, 2],
        [3, 4]
    ]
])

arr2 = np.array([
    [
        [5, 6],
        [7, 8]
    ]
])
result = np.concatenate((arr1, arr2), axis=1)
print(result)
print(result.shape)