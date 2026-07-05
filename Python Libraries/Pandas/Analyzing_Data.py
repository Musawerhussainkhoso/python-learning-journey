import pandas as pd
Data = pd.read_excel(r"D:\Python 2026\python-learning-journey\Python Libraries\Pandas\pandas_practice_dataset(1).xlsx")
#head
print(f" Five top rows: \n {Data.head(5)}")#first 5 rows
#tail
print(f" Five bottom rows: \n {Data.tail(5)}")#last 5 rows
#info
print(f" Information about the DataFrame: \n {Data.info()}")#information about the DataFrame
#describe 
print(f" Description of the DataFrame: \n {Data.describe()}")#description of the DataFrame
#shape
print(f" Shape of the DataFrame: \n {Data.shape}")#shape of the DataFrame
#columns 
print(f" Columns of the DataFrame: \n {Data.columns}")#columns of the DataFrame
#isnull
print(f" Check for null values: \n {Data.isnull().sum()}")#check for null values
#duplicated
print(f" Check for duplicated values: \n {Data.duplicated().sum()}")#check for duplicated values
