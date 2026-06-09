#Write a program that takes two sets from the user and finds the common elements.
set1 = set(input("Enter first set elements: ").split())
set2 = set(input("Enter second set elements: ").split())

common_elements = set1.intersection(set2)

print("Common elements:")
for item in common_elements:
    print(item)