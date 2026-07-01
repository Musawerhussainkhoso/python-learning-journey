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

'''
Create a 1D NumPy array containing numbers 5 to 50 (difference of 5).

Print:

First 4 elements
Elements from index 3 to the end
Middle four elements
'''
arr = np.array([5,10,15,20,25,30,35,40,45,50])

print("First 4 elements:", arr[:4])
print("From index 3 to end:", arr[3:])
print("Middle four elements:", arr[3:7])

'''
Create a 1D NumPy array containing numbers 100 to 1000 (difference of 100).

Print:

First 6 elements
Last 5 elements
Elements from index 1 to index 8
'''
arr = np.array([100,200,300,400,500,600,700,800,900,1000])

print("First 6 elements:", arr[:6])
print("Last 5 elements:", arr[-5:])
print("Index 1 to 8:", arr[1:9])
