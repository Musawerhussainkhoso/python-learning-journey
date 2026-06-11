#Store marks in a dictionary and calculate total and average using operators.
marks = {
    "Math": 85,
    "English": 78,
    "Physics": 90
}

total = sum(marks.values())
average = total / len(marks)

print("Total Marks:", total)
print("Average Marks:", average)