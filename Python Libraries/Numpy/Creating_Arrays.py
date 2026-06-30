import numpy as np
# From existing data
arr = np.array([1,2,3])
print(arr)

#Zeros
arr = np.zeros((3,4))
print(arr)

#Once
arr = np.ones((2,3))
print(arr)

#Range
arr = np.arange(0,10,2)
print(arr)

#Evenly Spaced Numbers(make numebrs on eqal distance)
arr = np.linspace(0, 10, 5)
print(arr)