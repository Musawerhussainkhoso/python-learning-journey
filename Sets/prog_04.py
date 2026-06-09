#Write a program that checks whether a given element exists in a set.
colors = {"red", "blue", "green", "yellow"}

color = input("Enter a color: ")

if color in colors:
    print("Color found!")
else:
    print("Color not found!")