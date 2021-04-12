def solve(n,target,arr):
    for val in arr:
        while str(traget) not in str(val):
            val-=traget
        if val>0:
            yield "YES"
        else:
            yield "NO"

for _ in range(int(input())):
    n,traget=map(int,input().split())
    arr=list(map(int,input().split()))
    for val in solve(n,traget,arr):
        print(val)