#Count Total Elements in Tuple
items = []

size = int(input("How many items? "))

for i in range(size):
    item = input(f"Enter item {i+1}: ")
    items.append(item)

items_tuple = tuple(items)

print("Tuple:", items_tuple)
print("Total Items:", len(items_tuple))