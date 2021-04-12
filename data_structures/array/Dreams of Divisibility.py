




for _ in range(int(input())):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    count=0
    for i in range(n):
        if arr[i]%k!=0:
            b=0
            for j in range(n):
                if (arr[i]+arr[j])%k==0:
                    b=1
                    break
            if b==1:
                count+=1
        else:
            count+=1
    if count==n:
        print("YES")
    else:
        print("NO")
