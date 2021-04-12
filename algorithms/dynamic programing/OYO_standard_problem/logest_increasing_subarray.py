def longest_increasing_subarray(arr):
    l=len(arr)
    dp=[1 for _ in range(l)]
    i=1

    while i<l:
        j=0
        while j<i:
            if arr[i]>arr[j]:
                dp[i]=max(dp[i],dp[j]+1)
            j+=1
        i+=1
    print(dp)

if __name__=="__main__":
    arr=[3,4,-1,0,6,2,3]
    longest_increasing_subarray(arr)