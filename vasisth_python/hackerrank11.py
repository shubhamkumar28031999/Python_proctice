no=int(input(""))
l=[]
for i in range(0,no):
    l2=list(map(str,input().strip().split(" ")))
    l.append(l2)
name=input("")
for i in range(0,no):
    if l[i][0]==name:
        sum=float(l[i][1])+float(l[i][3])+float(l[i][2])
        av=sum/3
        print("%.2f"%av)
