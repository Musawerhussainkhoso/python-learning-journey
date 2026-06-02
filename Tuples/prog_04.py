#Search an Element in Tuple
cities = []

size = int(input("How many cities? "))

for i in range(size):
    city = input("Enter city name: ")
    cities.append(city)

cities_tuple = tuple(cities)

search = input("Enter city to search: ")

if search in cities_tuple:
    print("City Found")
else:
    print("City Not Found")