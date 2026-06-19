#4. Using Else Block
try:
    num = int(input("Enter a number: "))
    result = 50 / num

except ZeroDivisionError:
    print("Cannot divide by zero!")

else:
    print("Division successful!")
    print("Result:", result)