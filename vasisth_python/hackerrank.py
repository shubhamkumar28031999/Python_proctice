list=[]
x,y=input("insert").split(" ")
list.insert(int(x),int(y))
x,y=input("insert").split(" ")
list.insert(int(x),int(y))
x,y=input("insert").split(" ")
list.insert(int(x),int(y))


print(list)
x=int(input("remove"))
list.remove(x)
x=int(input("append"))
list.append(x)
x=int(input("append"))
list.append(x)
list.sort()
print(list)
list.pop()
list.reverse()
print(list)