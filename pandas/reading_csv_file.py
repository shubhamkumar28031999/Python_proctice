import pandas as pd
df = pd.read_csv("reading_writing_csv\stock_data.csv")
print(df)
print("--------------------------------------------------------")
df1 = pd.read_csv("reading_writing_csv\stock_data.csv",skiprows=1)       # we can also do this by using header=1
print(df1)
print("--------------------------------------------------------")
df2 = pd.read_csv("reading_writing_csv\stock_data.csv",header=None)
print(df2)
print("--------------------------------------------------------")
df3 = pd.read_csv("reading_writing_csv\stock_data.csv",header=None,names=['akkad','bakkad','bambe','bol','sdhjkjsdf'])
print(df3)
print("--------------------------------------------------------")
df4 = pd.read_csv("reading_writing_csv\stock_data.csv",nrows=3)
print(df4)
print("--------------------------------------------------------")
df5 = pd.read_csv("reading_writing_csv\stock_data.csv",na_values=['not available','n.a.'])   #it will change all data into NaN
print(df5)
print("--------------------------------------------------------")
df6 = pd.read_csv("reading_writing_csv\stock_data.csv",  na_values={
        'eps': ['not available'],
        'revenue': [-1],
        'people': ['not available','n.a.'],
        'price':['n.a.']

    })
print(df6)