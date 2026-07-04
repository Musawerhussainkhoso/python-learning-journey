import pandas as pd
a = [1, 7, 2]

myvar = pd.Series(a)#series means one single column 

print(myvar)

#Simple Series Create and Print

numbers = pd.Series([10, 20, 30, 40, 50])

print(numbers)

#Series with Student Names

students = pd.Series(["Ali", "Sara", "Ahmed", "Majid"])

print(students)