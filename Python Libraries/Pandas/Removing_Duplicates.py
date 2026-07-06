import pandas as pd

data = {
    "Student_ID": [101, 102, 103, 104, 105, 102, 106, 107, 108, 101, 109, 110],
    
    "Name": ["Ali", "Sara", "Ahmed", "Hina", "Zain", "Sara", 
             "Usman", "Ayesha", "Bilal", "Ali", "Mehak", "Danish"],
    
    "City": ["Hyderabad", "Karachi", "Lahore", "Hyderabad", "Karachi", "Karachi",
             "Lahore", "Hyderabad", "Karachi", "Hyderabad", "Lahore", "Islamabad"],
    
    "Marks": [85, 90, 78, 88, 92, 90, 75, 95, 80, 85, 89, 91],
    
    "Department": ["CS", "SE", "IT", "CS", "SE", "SE",
                   "IT", "CS", "SE", "CS", "IT", "CS"]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

print("\nDuplicate rows:")
print(df[df.duplicated()])

print("\nDuplicate Student_ID:")
print(df[df.duplicated(subset=["Student_ID"])])

print("\nDuplicate count by Student_ID:")
print(df.duplicated(subset=["Student_ID"]).sum())

df_cleaned = df.drop_duplicates(subset=["Student_ID"], keep="first")
'''
keep = "first" means (duplicate records mein se pehla record rakho, baqi duplicate records remove kar do.)
'''
print("\nAfter removing duplicate Student_ID:")
print(df_cleaned)