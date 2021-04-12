def  LongestPalindromicSubstring(s):
    l=len(s)
    dp=[[0 for _ in range(l)] for _ in range(l)]
    for i in range(l):
        dp[i][i]=1
        if i<l-1 and s[i]==s[i+1]:
            dp[i][i+1]=1
    k=3
    

    for val in dp:
        print(val)


if __name__=="__main__":
    s="aaaabbaa"
    LongestPalindromicSubstring(s)