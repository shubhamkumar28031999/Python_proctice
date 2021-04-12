def longest_palindromic_subsequence(string1):
    string2=string1[::-1]
    l=len(string1)
    dp = [[0 for _ in range(l+1)] for _ in range(l+1)]
    for i in range(1,l+1):
        for j in range(1,l+1):
            if string1[i-1]==string2[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i][j-1],dp[i-1][j])
    for val in dp:
        print(val)



longest_palindromic_subsequence("akasdf")
