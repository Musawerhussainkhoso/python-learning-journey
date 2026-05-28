#Take numbers from user and find the largest.
numbers = []

size = int(input("How many numbers? "))

for i in range(size):
    num = int(input("Enter number: "))
    numbers.append(num)

largest = max(numbers)

print("Largest number:", largest)