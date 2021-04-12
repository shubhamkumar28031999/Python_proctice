lst=list(map(str,input("").split(" ")))
for i in range(0,len(lst)):
    lst[i]=lst[i].title()
for i in lst:
    print(i,end=" ")
