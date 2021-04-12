def solve(H,x,arr):
    for val in arr:
        if val+x==H:
            return True
    return False
N,H,x=map(int,input().split())
arr=list(map(int,input().split()))
if solve(H,x,arr):
    print("YES")
else:
    print("NO")