def solution(arr):
    l=len(arr)
    if l==0:
        return 0
    elif l==1:
        return arr[0]
    elif l==2:
        return max(arr)
    else:
        dp=[0]*l
        dp[0]=arr[0]
        dp[1]=max(arr[:2])
        for i in range(2,l):
            dp[i]=max(arr[i]+dp[i-2],dp[i-1])
        return dp[-1]



if __name__=="__main__":
    arr=[6, 7, 1, 3, 8, 2, 4]

    print(solution(arr))