from collections import Counter
for _ in range(int(input())):
    n,m=map(int,input().split())
    intial=list(map(int,input().split()))
    final=list(map(int,input().split()))
    painter=list(map(int,input().split()))
    count=Counter(final)
    if len(count)>m:
        print("NO")
    else:
        print("YES")
        