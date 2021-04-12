no=int(input(""))
a=[]
a.append(list(map(int,input().split(" "))))
positive=0
negative=0

zero=0
for i in a[0][0:no]:
    if i<0:
        negative+=1
    if i>0:
        positive+=1
    if i==0:
        zero+=1
print(positive/no)
print(negative/no)
print(zero/no)
