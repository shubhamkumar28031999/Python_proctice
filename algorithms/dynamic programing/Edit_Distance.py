def edit_distance(str_1,str_2,str_1_len,str_2_len):
    if str_1_len==0:
        return str_1_len
    if str_2_len==0:
        return str_2_len
    if str_1[str_1_len-1]==str_2[str_2_len-1]:
        return edit_distance(str_1,str_2,str_1_len-1,str_2_len-1)
    return 1+min(
        edit_distance(str_1, str_2, str_1_len, str_2_len - 1), #for addition
        edit_distance(str_1, str_2, str_1_len - 1, str_2_len), #for remove
        edit_distance(str_1, str_2, str_1_len - 1, str_2_len - 1) #for change
    )

def edit_distance_memorization(str_1,str_2,str_1_len,str_2_len):
    dp=[[0 for x in range(str_2_len+1)] for x in range(str_1_len+1)]
    for i in range(str_1_len+1):
        for j in range(str_2_len+1):
            if i==0:
                dp[i][j]=j
            if j==0:
                dp[i][j]=i
            if str_1[i-1]==str_2[j-1]:
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j]=1+min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])
    return dp[str_1_len][str_2_len]



if __name__=="__main__":
    for _ in range(int(input())):
        str_1_len,str_2_len=map(int,input().strip().split())
        str_1,str_2=map(str,input().strip().split())
        print(edit_distance_memorization(str_1,str_2,str_1_len,str_2_len))
