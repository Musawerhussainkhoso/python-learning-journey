import pandas as pd

# Step 1: Create data
data = {
    "Student": ["Ali", "Sara", "Ahmed", "Hina", "Zain", "Usman"],
    "Department": ["SE", "CS", "SE", "CS", "SE", "CS"],
    "City": ["Hyderabad", "Karachi", "Hyderabad", "Karachi", "Sukkur", "Hyderabad"],
    "Marks": [85, 90, 78, 88, 92, 75],
    "Fee": [5000, 6000, 5000, 6000, 5500, 5800]
}

# Step 2: Convert data into DataFrame
df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Step 3: Group by Department and find average marks
department_average = df.groupby("Department")["Marks"].mean()

print("\nAverage Marks Department Wise:")
print(department_average)

# Step 4: Group by Department and find total fee
department_fee = df.groupby("Department")["Fee"].sum()

print("\nTotal Fee Department Wise:")
print(department_fee)

# Step 5: Group by City and count students
city_students = df.groupby("City")["Student"].count()

print("\nNumber of Students City Wise:")
print(city_students)

# Step 6: Multiple calculations
department_summary = df.groupby("Department").agg({
    "Marks": ["mean", "max", "min"],
    "Fee": "sum"
})

print("\nDepartment Wise Summary:")
print(department_summary)