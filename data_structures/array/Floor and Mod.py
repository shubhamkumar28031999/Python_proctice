import math
for _ in range(int(input())):
    n,m=map(int,input().split())
    count=0
    for b in range(1,m+1):
        for a in range(1,n+1):
            x=a//b
            if x>b:
                break
            else:
                if x==a%b:
                    # print(a,b)
                    count+=1
    print(count)