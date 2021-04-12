import pandas as pd
df= pd.read_csv('weather1.csv')
print(df)

# df2=pd.read_excel("weather1.xlsx","Sheet1")
# print(df2)
print("---------------------------another maethod----------------------------------")
weather_data = {
    'day': ['1/1/2017','1/2/2017','1/3/2017'],
    'temperature': [32,35,28],
    'windspeed': [6,7,2],
    'event': ['Rain', 'Sunny', 'Snow']
}
df3 = pd.DataFrame(weather_data)
print(df3)
print("---------------------------another maethod----------------------------------")
weather_data = [
    ('1/1/2017',32,6,'Rain'),       #complete one row
    ('1/2/2017',35,7,'Sunny'),
    ('1/3/2017',28,2,'Snow')
]
df4 = pd.DataFrame(data=weather_data, columns=['day','temperature','windspeed','event'])
print(df4)
print("---------------------------another maethod----------------------------------")
weather_data = [
    {'day': '1/1/2017', 'temperature': 32, 'windspeed': 6, 'event': 'Rain'},
    {'day': '1/2/2017', 'temperature': 35, 'windspeed': 7, 'event': 'Sunny'},
    {'day': '1/3/2017', 'temperature': 28, 'windspeed': 2, 'event': 'Snow'},

]
df5 = pd.DataFrame(data=weather_data, columns=['day', 'temperature', 'windspeed', 'event'])
print(df5)