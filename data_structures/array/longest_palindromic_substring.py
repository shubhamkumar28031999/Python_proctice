def longest_palindromic_substring(s):
    l=len(s)
    rev_s=s[::-1]
    dp=[[0 for _ in range(l+1)] for _ in range(l+1)]
    max_len=0
    tub=[]
    for i in range(1,l+1):
        for j in range(1,l+1):
            if s[i-1]==rev_s[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
                max_len=max(max_len,dp[i][j])
                if dp[i][j]==max_len:
                    tub=[i,j]
    i=tub[0]
    j=tub[1]
    substring=""
    while dp[i][j]>=1:
        substring+=s[i-1]
        print(substring)
        i-=1
        j-=1
    return substring



s='babad'
longest_palindromic_substring(s)
