import math
def solve(n,arr):
    d={}
    for val in arr:
        if val[0] in d:
            d[val[0]].append(val[1:])
        else:
            d[val[0]]=[val[1:]]


for _ in range(int(input())):
    n=int(input())
    arr=list(map(str,input().split()))
    print(solve(n,arr))



