def fabonachi(num, dp):
    if num in dp:
        return dp[num]
    else:
        if num == 0:
            dp[0] = 0
            return 0
        if num == 1:
            dp[1] = 0
            return 1
        else:
            val = fabonachi(num - 1, dp) + fabonachi(num - 2, dp)
            dp[num] = val
            return val


if __name__ == "__main__":
    t = int(input())
    dp = dict()

    for i in range(t):
        num = int(input())
        for j in range(1, num + 1):
            if j in dp:
                print(dp[j], end=" ")
            else:
                val = fabonachi(j, dp)
                dp[j] = val
                print(val, end=" ")
        print()