import math
for _ in range(int(input())):
    n=int(input())
    i=1
    arr=[]
    sum=0
    for j in range(1,int(math.sqrt(n))+1):
        sum+=j*j
        # print(sum)
        i+=1
    k=int(math.sqrt(n))
    print(n-(k*(k-1))//2)
    for _ in range(n-int(math.sqrt(n))**2-1):
        sum+=i
    # print(sum)

