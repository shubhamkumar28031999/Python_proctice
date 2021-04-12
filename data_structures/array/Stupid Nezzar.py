for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    for _ in range(int(input())):
        s=input()
        if s=="U":
            for val in arr:
                print(val,end=" ")
            print()
        else:
            l,r,k=map(int,s.split())
            for i in range(l-1,r):
                arr[i]+=k

