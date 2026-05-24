#Take a number from the user and print its multiplication table using a while loop.
number = int(input("Enter a number: "))

i = 1

while i <= 10:
    print(number, "x", i, "=", number * i)
    i += 1