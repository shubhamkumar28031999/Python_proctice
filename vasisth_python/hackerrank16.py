x=int(input(""))
y=int(input(""))
z=int(input(""))
lst1=[]
q=int(input(""))
for j in range(0,x+1):
    for k in range(0,y+1):
        for l in range(0,z+1):
            lst=[]
            lst.append(j)
            lst.append(k)
            lst.append(l)
            lst1.append(lst)
lst2=[]
for i in lst1:
    if sum(i)!=q:
        lst2.append(i)
print(lst2)