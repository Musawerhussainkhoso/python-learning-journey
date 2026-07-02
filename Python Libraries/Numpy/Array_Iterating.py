import numpy as np 
#1D Array 
arr = np.array([1,2,3,4,5])
for i in arr:
    print(i)
    
#2D Array
arr = np.array([[1,2,3],
                [4,5,6]])
for i in arr:
    print(i)# In a 2D array, simple loop gives you row by row, not single values.
print("Printing each element in 2D array:")    
for i in arr:
    for j in i:
        print(j)
        
#3D Array 
arr = np.array([
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9],
        [10, 11, 12]
    ],
    [
        [13, 14, 15],
        [16, 17, 18]
    ],
    [
        [19, 20, 21],
        [22, 23, 24]
    ],
    [
        [25, 26, 27],
        [28, 29, 30]
    ],
    [
        [31, 32, 33],
        [34, 35, 36]
    ],
    [
        [37, 38, 39],
        [40, 41, 42]
    ]
])
print("/n Shape of the array: ",arr.shape)
for i in arr:
    print("This printing only blocks : ",i)
print("Printing each element in 3D array:")
for i in arr:
    for j in i:
        for k in j:
            print(k)    
            