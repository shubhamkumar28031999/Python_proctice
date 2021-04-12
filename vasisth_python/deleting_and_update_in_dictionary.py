user_info={
    'name':'shubham',
    'age': 19,
    'fav_movies':['avengers','iron man'],
    'fav_songs':['on my way','tum hi ho']
    }

poped_item=user_info.pop('age')     #don't do pop() it takes one argument
print(user_info)
print(poped_item)



poped_item=user_info.popitem()
print(user_info)
print(poped_item)


more_info={'name':'akash','state':'uttar pradesh'}
user_info.update(more_info)
print(user_info)