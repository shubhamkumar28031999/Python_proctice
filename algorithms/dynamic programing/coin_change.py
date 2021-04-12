def minmum_coin_excahange(arr,len_of_coins,total):
    dp=[[0 for x in range(total+1)] for x in range(len_of_coins)]
    for i in range(len_of_coins):
        for j in range(1,total+1):
            if i==0:
                if j%arr[i]==0:
                    dp[i][j]=j//arr[i]
                else:
                    dp[i][j]=0
            else:
                if arr[i]>j:
                    dp[i][j] = dp[i - 1][j]
                elif arr[i]==j:
                    dp[i][j]=1
                elif arr[i]<j:
                    # print(min(dp[i - 1][j], 1 + dp[i][j-arr[i]]))
                    dp[i][j] = min(dp[i - 1][j], 1 + dp[i][j-arr[i]])
        print(dp[i])


def count(S, m, n):
    table = [[0 for x in range(m)] for x in range(n + 1)]
    for i in range(m):
        table[0][i] = 1
    for i in range(1, n + 1):
        for j in range(m):
            x = table[i - S[j]][j] if i - S[j] >= 0 else 0
            y = table[i][j - 1] if j >= 1 else 0
            table[i][j] = x + y
    for val in table:
        print(val)
    return table[n][m - 1]

def max_count(arr,len_of_coins,total):
    dp = [[0 for x in range(total + 1)] for x in range(len_of_coins)]
    for i in range(len_of_coins):
        dp[i][0]=1
    for i in range(len_of_coins):
        for j in range(1, total + 1):
            if i == 0:
                if j % arr[i] == 0:
                    dp[i][j] =1
                else:
                    dp[i][j] = 0
            else:
                if arr[i] > j:
                    dp[i][j] = dp[i - 1][j]
                elif arr[i] <= j:
                    # print(min(dp[i - 1][j], 1 + dp[i][j-arr[i]]))
                    dp[i][j] = dp[i - 1][j]+ dp[i][j - arr[i]]
        print(dp[i])


def count_method_3(arr,len_of_coins,total):   #most efficient way
    dp = [0 for k in range(total + 1)]
    dp[0] = 1
    for i in range(0, len_of_coins):
        for j in range(arr[i], total + 1):
            dp[j] += dp[j - arr[i]]
    # print(dp)
    return dp[total]

if __name__=="__main__":
    # for _ in range(int(input())):
    len_of_coins=4
    arr=[1,2,5,10]
    total=50
    print(count_method_3(sorted(arr),len_of_coins,total))