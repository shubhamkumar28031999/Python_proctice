import pandas as pd

df = pd.read_csv('handle_missing_data\weather_data.csv',parse_dates=['day']) #before parsing day was in str format

print(type(df.day[0]))

df.set_index('day',inplace=True)
print(df)
print("========================================")
new_df=df.fillna(0)
print(new_df)
print("========================================")
new_df=df.fillna({
    'temperature' : 0,
    'windspeed':0,
    'event':'no event'
})
print(new_df)
print("========================================")
new_df=df.fillna(method="ffill")      #this is forward fill   #simillary for back fill bfill
print(new_df)
print("========================================")
new_df=df.fillna(method="bfill",axis='columns')      #it fill the values from the next column
print(new_df)
print("========================================")
new_df=df.fillna(method="ffill",limit=1)      #this will copy only once
print(new_df)
print("========================================")
new_df=df.interpolate()
print(new_df)
print("========================================")
new_df=df.interpolate(method='time')   #interpolated according to time
print(new_df)
print("========================================")
new_df=df.dropna()
print(new_df)
print("========================================")
new_df=df.dropna(how="all") #this will remove only one row which has only N.A values
print(new_df)
print("========================================")
new_df=df.dropna(thresh=2) #this will remove those rows which has two valid values
print(new_df)