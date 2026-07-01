'''
Question 1
Create a 1D NumPy array containing numbers 10 to 100 (difference of 10).

Print:

First 5 elements
Last 3 elements
Elements from index 2 to index 6
'''
import numpy as np

arr = np.array([10,20,30,40,50,60,70,80,90,100])

print("First 5 elements:", arr[:5])
print("Last 3 elements:", arr[-3:])
print("Index 2 to 6:", arr[2:7])
