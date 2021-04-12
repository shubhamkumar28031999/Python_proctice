for _ in range(int(input())):
    n,m=map(int,input().split())
    arr=list(map(int,input().split()))
    boulder=[]
    i=0
    flag=True
    while i<m and flag:
        k=0
        while k<n-1:
            if arr[k]>=arr[k+1]:
               k+=1
            else:
                arr[k]+=1
                boulder.append(k+1)
                break
        if k+1==n:
            flag=False
            break
        i+=1

    if flag and i==m:
        print(boulder[-1])
    else:
        print(-1)

