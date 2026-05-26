#Count Spaces in String
text = input("Enter a string: ")

spaces = 0

for char in text:

    if char == " ":
        spaces += 1

print("Total spaces:", spaces)