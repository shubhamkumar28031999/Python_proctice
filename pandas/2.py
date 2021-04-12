import pandas as pd
df = pd.read_csv('weather.csv')
print(df.shape)
rows, columns=df.shape
print(rows)
print(columns)
print("-------------------head-----------------------")
print(df.head())
print("--------------------tail---------------------")
print(df.tail(7))  #if not specciified it will show 5 values
print("--------------------slicing---------------------")
print(df[4:8])
print(df.columns)
print(df.Events)   #or you can use df.['Events']
print("--------------------limited columns---------------------")
print(df[['EST','Events']])
print(f" standard diviation {df['Temperature'].std()}")  #standard diviation
print("--------------------desribe---------------------")
print(df.describe())
