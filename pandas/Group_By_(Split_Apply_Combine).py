import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("Group_By_(Split_Apply_Combine)\weather_by_cities.csv")
print(df)
new_df= df.groupby('city')
for city,city_df in new_df:
    print(city)
    print(city_df)
print("+================mumbai====================")
print(new_df.get_group("mumbai"))
print("+================max====================")
print(new_df.max())
print("+================mean====================")
print(new_df.mean())
print("+================describe====================")
print(new_df.describe())
