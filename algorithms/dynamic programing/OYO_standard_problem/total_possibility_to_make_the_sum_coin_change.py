def total_possible_ways(arr,total):
    l=len(arr)
    dp=[[0 for _ in  range(total+1)] for _ in range(l)]
    for i in range(l):
        dp[i][0]=1
    for i in range(l):
        for j in range(total+1):
            if i ==0:
                if j%arr[i]==0:
                    dp[i][j]=1
            else:
                dp[i][j]=dp[i-1][j]+dp[i][j-arr[i]]
    for val in dp:
        print(val)


total_possible_ways([1,2,3],5)


