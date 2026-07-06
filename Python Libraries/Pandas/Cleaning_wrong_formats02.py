#Clean Numeric Format
import pandas as pd
import numpy as np

data = {
    "Product_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110,
                   111, 112, 113, 114, 115],

    "Product_Name": ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer",
                     "USB Cable", "Headphones", "Webcam", "Speaker", "Hard Drive",
                     "SSD", "RAM", "Router", "Power Bank", "Charger"],

    "Price": [
        "85,000",
        "Rs 1,500",
        "2,800",
        "Rs 25,000",
        "18000",
        "abc",
        np.nan,
        "7,500 PKR",
        "4,200",
        "Rs 12,000",
        "",
        "9,800",
        "15,000",
        "Rs 6,500",
        "wrong"
    ],

    "Quantity": [
        "10",
        "25 pcs",
        "30",
        "15 pieces",
        "8",
        "50",
        np.nan,
        "20 units",
        "abc",
        "",
        "12",
        "40 pcs",
        "18",
        "22",
        "wrong"
    ],

    "Discount": [
        "10%",
        "5%",
        "0%",
        "15%",
        np.nan,
        "20 percent",
        "",
        "8%",
        "abc",
        "12%",
        "5 percent",
        "10%",
        "0%",
        "wrong",
        "7%"
    ],

    "Rating": [
        "4.5",
        "4.0 stars",
        "3.8",
        "5 stars",
        "4.2",
        np.nan,
        "bad",
        "3.5 stars",
        "",
        "4.8",
        "4.1",
        "3.9 stars",
        "wrong",
        "4.6",
        "5"
    ]
}
df = pd.DataFrame(data)
print("Before Cleaning:")
print(df)
print(df.info())
print(df.isnull().sum())
df["Price"]= df["Price"]

# Price cleaning
df["Price"] = df["Price"].replace(r"[^0-9.]", "", regex=True)
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")
#0 se 9 tak numbers aur decimal point ke ilawa sab kuch remove kar do.
'''
Column ko real number mein convert karo.
Jo value number nahi ban sakti, usko NaN bana do.
'''
# Quantity cleaning
df["Quantity"] = df["Quantity"].replace(r"[^0-9.]", "", regex=True)
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")

# Discount cleaning
df["Discount"] = df["Discount"].replace(r"[^0-9.]", "", regex=True)
df["Discount"] = pd.to_numeric(df["Discount"], errors="coerce")

# Rating cleaning
df["Rating"] = df["Rating"].replace(r"[^0-9.]", "", regex=True)
df["Rating"] = pd.to_numeric(df["Rating"], errors="coerce")

print("After Format Cleaning:")
print(df)
print(df.info())
print(df.isnull().sum())

# Step 3: Fill missing values
df["Price"] = df["Price"].fillna(df["Price"].median())
df["Quantity"] = df["Quantity"].fillna(df["Quantity"].median())
df["Discount"] = df["Discount"].fillna(df["Discount"].median())
df["Rating"] = df["Rating"].fillna(df["Rating"].mean())

print("Final Cleaned Data:")
print(df)
print(df.info())
print(df.isnull().sum())

# Step 4: Save cleaned data
df.to_excel("cleaned_numeric_data.xlsx", index=False)

print("Cleaned numeric data saved successfully.")

