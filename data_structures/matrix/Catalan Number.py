def catlen_number(n):
    if n==0 or n==1:
        return 1
    else:
        arr=[0 for _ in range(n+1)]
        arr[0]=arr[1]=1
        for i in range(2,n+1):
            for j in range(i):
                arr[i]+=arr[j]*arr[i-j-1]
        print(arr[n])

catlen_number(3)
