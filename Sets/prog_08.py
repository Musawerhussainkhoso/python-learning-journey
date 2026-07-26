#Online Shopping
electronics = {"Ali", "Sara", "Ahmed", "Bilal"}
clothing = {"Sara", "Bilal", "Usman"}

print("Both:", electronics.intersection(clothing))
print("Only Electronics:", electronics.difference(clothing))
print("Only Clothing:", clothing.difference(electronics))
print("All Customers:", electronics.union(clothing))
print("Exactly One Category:", electronics.symmetric_difference(clothing))