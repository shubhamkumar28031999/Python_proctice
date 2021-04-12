no= int(input(""))
lst=[]
for i in range(0,no):
    lst2=[]
    lst2.append(input(""))
    lst2.append(float(input("")))
    lst.append(lst2)
lst3=[]
for i in range(0,no):
     lst3.append(lst[i][1])
lst3=set(lst3)
lst3=list(lst3)
lst3.sort()
lst4=[]
for i in range(0,no):
    if lst3[1]==lst[i][1]:
        lst4.append(lst[i][0])
    else:
        continue
lst4.sort()
for i in range(0,len(lst4)):
    print(lst4[i])

