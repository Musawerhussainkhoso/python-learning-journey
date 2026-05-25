#break
while True:

    number = int(input("Enter a number (0 to exit): "))

    if number == 0:
        print("Program ended")
        break

    print("You entered:", number)

#continue
subjects = int(input("How many subjects? "))

for i in range(subjects):

    marks = int(input(f"Enter marks for subject {i+1}: "))

    if marks < 0:
        print("Negative marks skipped")
        continue

    print("Marks recorded:", marks)

#pass
students = int(input("Enter number of students: "))

for i in range(students):

    name = input(f"Enter student {i+1} name: ")

    if name == "":
        pass

    print("Student:", name)