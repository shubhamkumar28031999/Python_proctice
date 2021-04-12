if __name__=="__main__":
    n=int(input())
    s=input()
    dp=dict()
    ma=0
    for i in range(n):
        if s[i] not in dp:
            dp[s[i]]=1
            ma=max(ma,dp[s[i]])
        else:
            dp[s[i]] += 1
            ma = max(ma, dp[s[i]])
    print(ma)