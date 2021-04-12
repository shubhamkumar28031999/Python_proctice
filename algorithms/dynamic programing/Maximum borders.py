if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        arr=[]
        for _ in range(n):
            arr.append(input())
        dp=[]
        for _ in range(n):
            z=[]
            for _ in range(m):
                z.append([0,0])
            dp.append(z)
        max_count=0
        for i in range(n):
            for j in range(m):
                if i==0:
                    if j==0:
                        if arr[i][j]=='#':
                            dp[i][j]=[1,1]
                    else:
                        if arr[i][j] == '#':
                            if arr[i][j-1]=='#':
                                dp[i][j][0]=dp[i][j-1][0]+1
                                dp[i][j][1]=1
                            else:
                                dp[i][j] = [1, 1]
                else:
                    if j==0:
                        if arr[i][j]=='#':
                            dp[i][j][0]=1
                            if arr[i-1][j]=='#':
                                dp[i][j][1]=dp[i-1][j][1]+1
                            else:
                                dp[i][j][1] = 1
                    else:
                        if arr[i][j]=='#':
                            if arr[i][j-1]=='#':
                                dp[i][j][0]=dp[i][j-1][0]+1
                            else:
                                dp[i][j][0] =  1
                            if arr[i - 1][j] == '#':
                                dp[i][j][1] = dp[i - 1][j][1] + 1
                            else:
                                dp[i][j][1] = 1

                max_count=max(max_count,max(dp[i][j]))
            print(dp[i])
        print(max_count)

        # ..  #####....
        # .  #######...
        # ......  # ....
        # ....  #####..
        # ...  #####...