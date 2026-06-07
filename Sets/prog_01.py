#Store Unique Favorite Fruits
fruits = set()

for i in range(5):
    fruit = input("Enter a fruit: ")
    fruits.add(fruit)

print("Unique fruits are:")
print(fruits)