import pandas as pd
data = {
    "Employee_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "Employee_Name": ["Ali", "Sara", "Ahmed", "Hina", "Bilal", "Ayesha", "Hamza", "Zain", "Noor", "Usman"],
    "Department": ["IT", "HR", "Finance", "IT", "Finance", "HR", "IT", "Finance", "HR", "IT"],
    "City": ["Karachi", "Lahore", "Karachi", "Islamabad", "Lahore", "Karachi", "Lahore", "Islamabad", "Karachi", "Lahore"],
    "Gender": ["Male", "Female", "Male", "Female", "Male", "Female", "Male", "Male", "Female", "Male"],
    "Salary": [85000, 65000, 90000, 95000, 78000, 70000, 88000, 82000, 72000, 91000],
    "Experience_Years": [3, 2, 5, 4, 3, 2, 6, 4, 1, 5],
    "Performance_Rating": [4.2, 4.0, 4.5, 4.7, 3.9, 4.1, 4.8, 4.3, 3.8, 4.6]
}

df = pd.DataFrame(data)
print(df)

# 1. Department wise average salary
print(df.groupby("Department")["Salary"].mean())

# 2. City wise total salary
print(df.groupby("City")["Salary"].sum())

# 3. Department wise employees count
print(df.groupby("Department")["Employee_Name"].count())

# 4. Gender wise average performance rating
print(df.groupby("Gender")["Performance_Rating"].mean())

# 5. Department wise maximum salary
print(df.groupby("Department")["Salary"].max())

# 6. City wise average experience
print(df.groupby("City")["Experience_Years"].mean())

# 7. Department and Gender wise average salary
print(df.groupby(["Department", "Gender"])["Salary"].mean())