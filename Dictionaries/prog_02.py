#Ask the user to enter 3 subjects and their marks, then store them in a dictionary.
marks = {}

for i in range(3):
    subject = input("Enter subject name: ")
    score = int(input("Enter marks: "))
    marks[subject] = score

print("\nMarks Dictionary:")
print(marks)