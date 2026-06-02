#Count Even Numbers in Tuple
numbers = []

size = int(input("How many numbers? "))

for i in range(size):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

numbers_tuple = tuple(numbers)

count = 0

for num in numbers_tuple:

    if num % 2 == 0:
        count += 1

print("Even Numbers:", count)