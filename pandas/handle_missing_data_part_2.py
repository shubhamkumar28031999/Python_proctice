import pandas as pd
import  numpy as np
df = pd.read_csv('handle_missing_data_part_2\weather_data.csv')
print(df)
print("=================================================")
new_df = df.replace([-99999,-888888],np.NaN)
print(new_df)
print("=================================================")
new_df = df.replace({
    -99999:np.NaN,
    'No Event': 'Sunny'
})
print(new_df)
print("=================================================")
new_df = df.replace({
    'temperature':'[A-Za-z]',
    "windspeed":'[A-Za-z]'
},'',regex=True)        #this will replace all the character with the space  ""
print(new_df)