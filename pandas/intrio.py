import pandas as pd
data=pd.read_csv('weather.csv')
print(data)
print(data['Temperature'].max())
print(data['EST'][data['Events']== 'Rain'])
data.fillna(0,inplace=True)
print(f" wind speed is {data['WindSpeedMPH'].mean()}")