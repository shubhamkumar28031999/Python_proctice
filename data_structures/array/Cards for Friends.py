for _ in range(int(input())):
    w,h,n=map(int,input().split())
    count=0
    while w%2==0 or h%2==0:
        if w%2==0:
            count+=1
            w=w//2
        else:
            count+=1
            h=h//2
    print("YES" if 2**count>=n else "NO")