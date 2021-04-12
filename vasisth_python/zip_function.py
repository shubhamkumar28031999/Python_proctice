user_id=['user1','user2','user3']
names=['shubham','harshit','akash']
last_name=['kumar','vashistha','chaudhary']
print(dict(zip(user_id,names)))

example =[('a',1),('b',2)]
print(example)
print(list(zip(user_id,names,last_name)))

zip1=list(zip(user_id,names))
print(zip1)
print(list(zip(*zip1)))
l1,l2=list(zip(*zip1))
print(l1)
print(l2)


# for printing greater number iin both list
b1=[2,5,4,6,7]
b2=[4,3,5,7,2]
new_list=[]
for pair in zip(b1,b2):
    new_list.append(max(pair))
print(new_list)