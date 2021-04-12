import  math
for _ in range(int(input())):
    l,r=map(int,input().split())
    flag=True
    ans=2
    while flag:
        temp=True
        for i in range(l,r+1):
           if math.gcd(i,ans)!=1:
               temp=False
               break
        if temp:
            break
        ans+=1
    print(ans)
