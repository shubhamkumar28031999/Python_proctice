user1={'name':'shubham','age':20}
user2=dict(name='shubham',age=20)
print(user1)
print(user2)
print(user1['name'])
user_info={
    'name':'shubham',
    'age': 19,
    'fav_movies':['avengers','iron man'],
    'fav_songs':['on my way','tum hi ho']
    }
print(user_info)
print(user_info['fav_movies'])


#adding elemaents in dictionaries
user3={}
user3['name']='akash'
print(user3)
if 'name' in user_info:
    print("key present")
else:
    print("key not present")


if 'shubham' in user_info:
    print("value present")
else:
    print("value not present")

if 'shubham' in user_info.values():
    print("value present")
else:
    print("value not present")