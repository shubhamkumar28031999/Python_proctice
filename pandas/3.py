import pandas as pd
df = pd.read_csv('weather.csv')
print(df[df.Temperature>=40])
print(df[['EST','Temperature']][df.Temperature==df.Temperature.max()])
print(df.index)
df.set_index('EST',inplace=True)# inplace is use to apply the transformation for permanently
print(df)
print(df.loc['1/9/2016'])
df.reset_index(inplace=True)
print(df)