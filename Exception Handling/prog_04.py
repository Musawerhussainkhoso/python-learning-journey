#5. Using Finally Block
try:
    num = int(input("Enter a number: "))
    print(100 / num)

except ZeroDivisionError:
    print("Cannot divide by zero!")

finally:#finally always executes whether an exception occurs or not.
    print("Program execution completed.")