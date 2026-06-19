#3. Multiple Exceptions
try:
    num = int(input("Enter a number: "))
    result = 100 / num

    print("Result:", result)

except ValueError:
    print("Invalid input! Enter numbers only.")

except ZeroDivisionError:
    print("Cannot divide by zero!")