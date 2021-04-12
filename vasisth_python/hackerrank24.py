from collections import Counter
n=int(input(""))
num=list(map(int,input("").split(" ")))
count1=Counter(num)
count2=Counter(num).items()
for i in count2:
    count3=list(i)
n2=int(input(""))
total=0
for i in range(0,n2):
    num2 = list(map(int, input("").split(" ")))
    for m in count3:
        print(m)
        if num2[0]==m[0]:
            if m[0]>0:
                m[0]=m[0]-1
                total=total+m[1]
            if m[0]==0:
                m=0
print(total)

