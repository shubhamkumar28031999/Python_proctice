def func(item):
    return len(item)

names = ['harshit vashistha','z', 'mohit', 'akash']
print(min(names, key=func))
print(max(names, key=lambda item: len(item)))
# print(max(names))