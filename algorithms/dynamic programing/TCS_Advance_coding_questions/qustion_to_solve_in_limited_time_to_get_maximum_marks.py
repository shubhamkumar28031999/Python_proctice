def Knapsac_problem(total_time,marks,marks_Arr,time_arr,n):
    dp = [[0 for _ in range(total_time+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,total_time+1):
            if time_arr[i-1]>j:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=max(dp[i-1][j],marks_Arr[i-1]+dp[i-1][j-time_arr[i-1]])
    for val in dp:
        print(val)


if __name__=="__main__":
    total_time=10
    marks=10
    Marks_arr=[0, 6, 4, 2, 8]
    time_arr=[0, 4, 6, 2, 7 ]
    n=5
    Knapsac_problem(total_time,marks,Marks_arr,time_arr,n)


