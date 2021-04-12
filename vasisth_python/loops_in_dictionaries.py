user_info={
    'name':'shubham',
    'age': 19,
    'fav_movies':['avengers','iron man'],
    'fav_songs':['on my way','tum hi ho']
    }

for i in user_info:
    print(i)
print("-------------------")
for i in user_info.values():
    print(i)


user_info_values=user_info.values()
print(user_info_values)

user_info_keys=user_info.keys()
print(user_info_keys)

user_info_items=user_info.items()
print(user_info_items)

for key,value in user_info.items():
    print(f"key is {key} and value {value}")



