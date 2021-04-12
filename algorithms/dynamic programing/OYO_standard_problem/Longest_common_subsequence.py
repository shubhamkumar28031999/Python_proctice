def LCS(string1,string2):
    l1=len(string1)
    l2=len(string2)
    dp=[[0 for x in range(l2+1)] for _ in range(l1+1)]
    for i in range(1,l1+1):
        for j in range(1,l2+1):
            if string1[i-1]==string2[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    for val in dp:
        print(val)


if __name__=="__main__":
    string1="shubham"
    string2="shukla"
    LCS(string1,string2)
