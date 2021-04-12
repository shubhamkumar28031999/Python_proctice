import math
for _ in range(int(input())):
    n=int(input())
    weight=list(map(int,input().split()))
    jump=list(map(int,input().split()))
    d={}
    ans=0
    for i in range(1,n+1):
        d[i]=weight.index(i)
    for i in range(2,n+1):
        temp=0
        if d[i]<=d[i-1]:
            temp=math.ceil((d[i-1]-d[i]+1)/jump[d[i]])
        ans+=temp
        d[i]+=temp*(jump[d[i]])
    print(ans)