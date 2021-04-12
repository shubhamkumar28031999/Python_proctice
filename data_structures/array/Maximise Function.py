from itertools import combinations
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    a=arr[0]
    b=arr[-1]
    ans=0
    for i in range(1,n-1):
        ans=max(ans,abs(a-b)+abs(b-arr[i]) + abs(a-arr[i]))
    print(ans)