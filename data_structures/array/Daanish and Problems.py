def solve(arr):
    for i in range(9, -1, -1):
        if arr[i]>0:
            return i+1

for _ in range(int(input())):
    arr=list(map(int,input().split()))
    n=int(input())
    l=10
    for i in range(9,-1,-1):
        if n>0 and arr[i]>0:
            if n>arr[i]:
                n-=arr[i]
                arr[i]=0
            else:
                arr[i]-=n
                n=0
    print(solve(arr))