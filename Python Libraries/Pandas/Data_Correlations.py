import pandas as pd

# Step 1: Create sample data
data = {
    "Student": ["Ali", "Sara", "Ahmed", "Hina", "Zain", "Usman"],
    "Study_Hours": [2, 4, 5, 3, 6, 7],
    "Marks": [50, 65, 70, 60, 85, 90],
    "Sleep_Hours": [8, 7, 6, 7, 5, 4],
    "Mobile_Usage_Hours": [5, 4, 3, 4, 2, 1]
}

# Step 2: Convert data into DataFrame
df = pd.DataFrame(data)

# Step 3: Print full data
print("Student Data:")
print(df)

# Step 4: Find correlation between numeric columns
correlation = df.corr(numeric_only=True)

print("\nCorrelation Between Columns:")
print(correlation)
#0,1,-1
# Step 5: Find correlation between two specific columns
study_marks_corr = df["Study_Hours"].corr(df["Marks"])
sleep_marks_corr = df["Sleep_Hours"].corr(df["Marks"])
mobile_marks_corr = df["Mobile_Usage_Hours"].corr(df["Marks"])

print("\nStudy Hours and Marks Correlation:", study_marks_corr)
print("Sleep Hours and Marks Correlation:", sleep_marks_corr)
print("Mobile Usage and Marks Correlation:", mobile_marks_corr)