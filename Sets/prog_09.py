#University Courses
python_course = {1, 2, 3, 4, 5}
ai_course = {4, 5, 6, 7}

print("Both Courses:", python_course & ai_course)
print("Python Only:", python_course - ai_course)
print("AI Only:", ai_course - python_course)
print("Total Students:", python_course | ai_course)
print("AI Subset of Python:", ai_course.issubset(python_course))