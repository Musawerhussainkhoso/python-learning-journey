import numpy as np 
#1. Integer (i)
employee_ids = np.array([101, 102, 103, 104])

print(employee_ids)
print(employee_ids.dtype)

#2. boolean
attendance = np.array([True, False, True, True])
print(attendance)
print(attendance.dtype)

#unsigned integer
'''product_quantity = np.array([25, 40, 18, 60], dtype="u")

print(product_quantity)
print(product_quantity.dtype)'''

#float
student_gpa = np.array([3.45, 3.89, 2.95, 3.76])

print(student_gpa)
print(student_gpa.dtype)

#complex
electrical_signal = np.array([2+3j, 5+4j, 7+1j])

print(electrical_signal)
print(electrical_signal.dtype)

#6. Timedelta (m)
delivery_time = np.array([3, 7, 10], dtype="timedelta64[D]")

print(delivery_time)
print(delivery_time.dtype)

#7. Datetime (M)
joining_dates = np.array(
    ["2026-01-10", "2026-02-15", "2026-03-20"],
    dtype="datetime64[D]"
)

print(joining_dates)
print(joining_dates.dtype)

#8. Object (O)
employee_data = np.array([101, "Ali", True, 45000.75], dtype="O")

print(employee_data)
print(employee_data.dtype)

#9. String (S)
countries = np.array(["Pakistan", "India", "China"], dtype="S")

print(countries)
print(countries.dtype)

#10. Unicode String (U)
languages = np.array(["English", "اردو", "العربية"], dtype="U")

print(languages)
print(languages.dtype)

