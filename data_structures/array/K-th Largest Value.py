n,k=map(int,input().split())
arr=list(map(int,input().split()))
s=sum(arr)
for _ in range(k):
    a,b=map(int,input().split())
    if a==1:
        if arr[b-1]==1:
            s-=1
            arr[b-1]=0
        else:
            s+=1
            arr[b-1]=1
    if a==2:
        if s>=b:
            print(1)
        else:
            print(0)
