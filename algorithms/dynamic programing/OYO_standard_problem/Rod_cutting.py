def rod_cutting(arr,total):
    l=len(arr)
    dp=[[0 for _ in range(total+1)] for _ in range(l)]
    for i in range(l):
        for j in range(1,total+1):
            if i==0:
                dp[i][j]=arr[i]*j
            else:
                if j<i+1:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=max(dp[i-1][j],arr[i]+dp[i][j-i-1])
    for val in dp:
        print(val)

rod_cutting([2,5,7,8],5)