for _ in range(int(input())):
    l,r=map(int,input().split())
    if l==r:
        print(1)
    else:
        print((r-l)*2 +1)
