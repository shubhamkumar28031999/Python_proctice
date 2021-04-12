user_info={
    # 'name':'shubham',
    # 'age': 19,
    # 'fav_movies':['avengers','iron man'],
    # 'fav_songs':['on my way','tum hi ho']
    }
for i in range(0,100):
    key = input("enter the key")
    if key == str(-1):
        break
    else:
        value=input("enter the value")
        user_info[key]=value

for key ,value in user_info.items():
    print(f"{key}:{value}")