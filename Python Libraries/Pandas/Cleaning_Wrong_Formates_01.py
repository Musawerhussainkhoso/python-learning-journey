#CLEAN DATE FORMATS
import pandas as pd
import numpy as np

data = {
    "Order_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110,
                 111, 112, 113, 114, 115],

    "Customer_Name": ["Ali", "Sara", "Ahmed", "Hina", "Zain",
                      "Usman", "Ayesha", "Bilal", "Mehak", "Danish",
                      "Iqra", "Hamza", "Laiba", "Farhan", "Sana"],

    "Order_Date": [
        "2024-01-15",      # correct format
        "15-02-2024",      # day-month-year
        "03/10/2024",      # slash format
        "April 5, 2024",   # text month
        "2024/05/20",      # year/month/day
        "25 June 2024",    # day text month year
        "2024.07.12",      # dot format
        "08-15-2024",      # month-day-year
        "wrong date",      # wrong value
        "",                # empty value
        np.nan,            # missing value
        "2024-13-01",      # invalid month
        "2024-02-30",      # invalid day
        "10 Aug 2024",     # short month name
        "20240901"         # compact date
    ],

    "Amount": [2500, 3000, 1500, 4500, 5000,
               2800, 3500, 4200, 3900, 2100,
               6000, 3300, 2700, 3100, 4800]
}
df = pd.DataFrame(data)
print(df)
print(df.info())
#convert date column to datetime format
df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors='coerce')
print(df)
'''
Jo date correct hai → datetime ban jaaye
Jo date wrong hai → NaT ban jaaye
'''
#now check wrong invalid dates
print(df[df["Order_Date"].isna()])

print("----DECIDE WHAT TO DO WITH INVALID DATES----")
#option:01 remove the rows with invalid dates
df_cleaned = df.dropna(subset=["Order_Date"])#subset means to take descion based on specific column
print(df_cleaned)

#option 02: replace invalid dates with a default date
default_date = pd.Timestamp("2024-01-01")
print(df["Order_Date"].fillna(default_date))
