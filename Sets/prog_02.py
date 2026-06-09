#Write a program that takes numbers from the user and displays only the unique numbers.
numbers = input("Enter numbers separated by spaces: ").split()

unique_numbers = set(numbers)

print("Unique numbers are:")
for num in unique_numbers:
    print(num)