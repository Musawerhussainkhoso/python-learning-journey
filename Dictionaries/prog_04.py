#Count how many times each fruit appears in a list using a dictionary.
fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]

frequency = {}

for fruit in fruits:
    if fruit in frequency:
        frequency[fruit] += 1
    else:
        frequency[fruit] = 1

print("Fruit Frequency:")
print(frequency)