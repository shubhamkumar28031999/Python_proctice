def regular_expression( s, p):
    string_len=len(s)
    pattern_len=len(p)
    if pattern_len==0:
        return True if string_len==0 else False
    dp=[[False for _ in range(pattern_len+1)] for _ in range(string_len+1)]
    dp[0][0]=True
    for i in range(1,pattern_len+1):
        if p[i-1]=='*':
            dp[0][i]=dp[0][i-1]
    for i in range(1,string_len+1):
        for j in range(1,pattern_len+1):
            if p[j-1]=='*':
                dp[i][j]= dp[i-1][j] or dp[i][j-1]
            elif p[j-1]=="." or p[j-1]==s[i-1]:
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j]=False
    return dp[string_len][pattern_len]

def match(text, pattern):
    if not pattern: return not text
    # first_match = bool(text) and pattern[0] in {text[0], '.'}
    # return first_match and match(text[1:], pattern[1:])

if __name__=="__main__":
    s = "aa"

    p =""
    print(bool(s))
    print(match(s,p))