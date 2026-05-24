#Take a number from the user and print its multiplication table using a for loop.
number = int(input("Enter a number: "))

for i in range(1, 11):
    print(number, "x", i, "=", number * i)