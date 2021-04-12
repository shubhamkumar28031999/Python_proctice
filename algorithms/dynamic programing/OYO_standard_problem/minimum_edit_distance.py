def minium_number_of_edits(string1,string2):
    l1=len(string1)
    l2=len(string2)
    dp=[[0 for x in range(l1+1)] for _ in range(l2+1)]
    for i in range(l1+1):
        dp[0][i]=i
    for i in range(l2+1):
        dp[i][0]=i

    for i in range(1,l2+1):
        for j in range(1,l1+1):
            if string1[j-1]==string2[i-1]:
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j]=1+min([dp[i-1][j],dp[i-1][j-1],dp[i][j-1]])
    for val in  dp:
        print(val)

if __name__=="__main__":
    string1="abcdef"
    string2="azced"
    minium_number_of_edits(string1,string2)