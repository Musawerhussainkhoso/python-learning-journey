#Take a number from the user and count how many digits it contains using a while loop.
number = int(input("Enter a number: "))

count = 0

while number > 0:
    number = number // 10
    count += 1

print("Total digits:", count)