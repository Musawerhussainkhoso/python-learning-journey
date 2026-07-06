import pandas as pd
import numpy as np

data = {
    "Student_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110,
                   111, 112, 113, 114, 115, 116, 117, 118, 119, 120],

    "Name": ["Ali", "Sara", "Ahmed", "Hina", "Zain", "Usman", "Ayesha", "Bilal", "Mehak", "Danish",
             "Iqra", "Hamza", "Laiba", "Farhan", "Sana", "Taha", "Nimra", "Asad", "Mariam", "Rehan"],

    "Age": [20, 21, np.nan, 22, 20, 23, 21, np.nan, 22, 24,
            20, 21, 23, 22, np.nan, 25, 21, 22, 20, 23],

    "City": ["Hyderabad", "Karachi", "Hyderabad", np.nan, "Lahore", "Hyderabad", "Karachi", "Hyderabad", np.nan, "Islamabad",
             "Hyderabad", "Karachi", "Lahore", "Hyderabad", "Karachi", np.nan, "Hyderabad", "Lahore", "Karachi", "Hyderabad"],

    "Marks": [78, 85, np.nan, 90, 72, 88, 95, 80, np.nan, 91,
              76, 84, 79, 300, 82, np.nan, 89, 77, 86, 81],

    "Attendance": [85, 90, 78, np.nan, 88, 92, 95, 80, 76, np.nan,
                   84, 89, 91, 87, 82, 79, np.nan, 86, 90, 88],

    "Department": ["CS", "SE", "CS", "IT", np.nan, "SE", "CS", "SE", "IT", "CS",
                   "SE", np.nan, "CS", "IT", "SE", "CS", "CS", "SE", "IT", "CS"],

    "Fee": [25000, 27000, np.nan, 26000, 25500, 28000, 30000, np.nan, 26500, 100000,
            25000, 27500, 26000, 25500, np.nan, 29000, 28500, 27000, 26000, 25000]
}

df = pd.DataFrame(data)
print(df)
print(df.info())
print(df.isnull().sum())
#age
df["Age"] = df["Age"].fillna(df["Age"].mode()[0])
print(df)
#city
df["City"] = df["City"].fillna(df["City"].mode()[0])
print(df)
#marks
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
print(df)
#attendance
df["Attendance"] = df["Attendance"].fillna(df["Attendance"].mean())
print(df)
#Department
df["Department"] = df["Department"].fillna(df["Department"].mode()[0])
print(df)
#fee
df["Fee"] = df["Fee"].fillna(df["Fee"].mean())
print(df)