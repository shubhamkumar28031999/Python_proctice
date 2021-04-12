import sys
for _ in range(int(input())):
    n,v,u=map(int,input().split())
    l=len(set(map(int,input().split())))
    if l==1:
        print(v+u)
    else:
        print()

