def O_1_l_knapsack(wight_arr,item_val,total_wight):
    dp=[[0 for x in range(total_wight+1)] for _ in range(len(item_val))]
    for i in range(len(item_val)):
        for j in range(1,total_wight+1):
            if i==0:
                if j<len(wight_arr) and j==wight_arr[i]:
                    dp[i][j]=item_val[i]
                else:
                    dp[i][j]=dp[i][j-1]
            else:
                if wight_arr[i]>j:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=max(item_val[i] + dp[i][j-wight_arr[i]],dp[i-1][j])
    for val in dp:
        print(val)
    print(dp[len(item_val)-1][total_wight])


if __name__=="__main__":
    wight=[4,5,1]
    item_val=[1,2,3]
    O_1_l_knapsack(wight,item_val,4)