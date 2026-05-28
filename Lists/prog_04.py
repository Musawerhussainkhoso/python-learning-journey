#User enters fruits and program counts them.
fruits = []

total = int(input("How many fruits do you want to add? "))

for i in range(total):
    fruit = input(f"Enter fruit {i+1}: ")
    fruits.append(fruit)

print("Fruit List:", fruits)
print("Total Fruits:", len(fruits))