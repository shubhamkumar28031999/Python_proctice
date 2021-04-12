def factorial(n,dp):
    if n in dp:
        return dp[n]
    else:
        res=1
        dp[1]=1
        for i in range(2,n+1):
            res=res*i
            dp[i]=res
        return res
if __name__=="__main__":
    for _ in range(int(input())):
        n,r=map(int,input().strip().split())
        dp={}
        ans=factorial(n,dp)
        print(ans%((10**9)+7))