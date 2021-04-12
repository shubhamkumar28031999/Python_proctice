def min_coin_sum_prob(arr,total):
    len_arr=len(arr)
    dp=[0 for x in range(total+1)]
    dp[0]=0
    for i in range(len_arr):
        for j in range(arr[i],total+1):
            if j%arr[i]==0:
                dp[j]=j//arr[i]
            else:
                dp[j]=min(dp[j],1+dp[j-arr[i]])
    print(dp)

def check_if_sum_present_or_not(arr,total):
    l=len(arr)
    dp=[0 for x in range(total+1)]
    dp[0]=1
    for i in range(0,l):
        for j in range(arr[i],sum(arr[:i+1])+1):
            if j<=total:
                dp[j]=dp[j-arr[i]]
    print(dp)



if __name__=="__main__":
    arr=[1,3,5,10,12]
    total=23
    min_coin_sum_prob(arr,total)
