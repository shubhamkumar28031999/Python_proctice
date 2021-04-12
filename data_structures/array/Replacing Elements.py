def solve(arr,n,s):
    m=min(arr)
    for i in range(n-1):
        if arr[i]+m<=s:
            return 'YES'
    return 'NO'

for _ in range(int(input())):
    n,s=map(int,input().split())
    arr=list(map(int,input().split()))
    print(solve(arr,n,s))