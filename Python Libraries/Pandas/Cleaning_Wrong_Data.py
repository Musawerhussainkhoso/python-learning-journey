import pandas as pd 
import numpy as np
'''
Cleaning wrong data ka matlab hota hai:
Data ka format sahi hai, lekin value logically wrong hai.
Example:
Column	Wrong Data Example	Problem
Age	200	student ki age 200 nahi ho sakti
'''
data = {
    "Name": ["Ali", "Sara", "Ahmed", "Hina", "Zain"],
    "Age": [20, 21, 200, 22, 19],
    "Marks": [85, 90, 300, 78, 88],
    "Price": [1500, 2500, -500, 3000, 1800],
    "Rating": [4.5, 5.0, 8.0, 3.8, 4.2]
}
df = pd.DataFrame(data)
print(df)

print(df.loc[0, 'Age'])  # Accessing a specific value in the DataFrame
print(df.iloc[0,1])
#step 01 (identify wrong values)
print("Wrong Age Values:")
print(df[df['Age'] > 150])

print("Wrong Marks Values:")
print(df[df['Marks'] > 100])

print("Wrong Price Values:")
print(df[df['Price'] < 0])

print("Wrong Rating Values:")
print(df[df['Rating'] > 5])

#to fix the wrong values
df.loc[df["Age"] > 150, "Age"] = np.nan
df.loc[df["Marks"] > 100, "Marks"] = np.nan
df.loc[df["Price"] < 0, "Price"] = np.nan
df.loc[df["Rating"] > 5, "Rating"] = np.nan

print("After converting wrong values into NaN:")
print(df)

# Step 03: Fill NaN values with suitable values

df["Age"] = df["Age"].fillna(df["Age"].median())
df["Marks"] = df["Marks"].fillna(df["Marks"].median())
df["Price"] = df["Price"].fillna(df["Price"].median())
df["Rating"] = df["Rating"].fillna(df["Rating"].mean())
print("After fixing wrong values:")
print(df)

