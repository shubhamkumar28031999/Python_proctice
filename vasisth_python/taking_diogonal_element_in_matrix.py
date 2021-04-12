no=int(input(""))
ab=[]
for i in range(0,no):
    a=list(map(int,input().split(" ")))
    ab.append(a)
d1=0
d2=0
for i in range(0,no):
    d2=d2+ab[i][no-i-1]
    d1=d1+ab[i][i]
print(abs(d1-d2))

