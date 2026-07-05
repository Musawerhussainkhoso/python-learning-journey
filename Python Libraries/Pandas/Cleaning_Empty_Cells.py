import pandas as pd 
Data = pd.read_excel(r"D:\Python 2026\python-learning-journey\Python Libraries\Pandas\pandas_practice_dataset(1).xlsx")
#dropna ( By default, the dropna() method returns a new DataFrame, and will not change the original.)
df = Data.dropna()#drop all rows with any NaN values
'''print(df)
print("----------------------------------------------------")
print(Data)'''
print(df.head(5))
print(df.tail(5))
#Replace empty Values

