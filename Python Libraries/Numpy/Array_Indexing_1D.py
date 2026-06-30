import numpy as np 
#Access the First Element
arr = np.array([10, 20, 30, 40, 50])
print("First Element:", arr[0])

#Access the Last Element
arr = np.array([5, 10, 15, 20, 25])
print("Last Element:", arr[-1])

#Access Multiple Elements
arr = np.array([100, 200, 300, 400, 500])
print("First Element:", arr[0])
print("Third Element:", arr[2])
print("Fifth Element:", arr[4])

#Perform Calculation Using Indexed Elements
arr = np.array([8, 12, 20, 16, 24])
# Add first and third elements
result = arr[0] + arr[2]
print("First Element:", arr[0])
print("Third Element:", arr[2])
print("Sum:", result)