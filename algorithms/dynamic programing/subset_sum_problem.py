def sum_subset_exist_or_not_method_1(arr,arr_len,s):
    dp = [[0 for x in range(s+1)] for x in range(arr_len)]
    for x in range(arr_len):
        dp[x][0]=1
    for i in range(arr_len):
        for j in range(1,s+1):
            if i==0:
                if j==arr[i]:
                    dp[i][j]=1
            else:
                if j<arr[i]:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j-arr[i]] if dp[i-1][j]==0 else 1
    return dp[arr_len][s]


def sum_subset_exist_or_not_method_2(arr,arr_len,s):
    dp = [0 for x in range(s+1)]
    dp[0]=1
    for i in range(arr_len):
        for j in range(arr[i],sum(arr[:i+1])):
            if j<=s:
                dp[j]=dp[j-arr[i]] if dp[j]==0 else 1
    return dp[s]


def check_if_two_suset_have_same_sum(arr,arr_len):
    if len(arr)==0:
        return False
    sum_arr=sum(arr)
    if sum_arr%2==1:
        return False
    return sum_subset_exist_or_not_method_2(arr,arr_len,sum_arr//2)

def minimum_subset_sum_diffrence(arr):
    sum_all=sum(arr)
    minimum=10**9
    for i in range(sum_all+1):
        if sum_subset_exist_or_not_method_2:
            minimum=min(abs(sum_all-i-i),minimum)
    print(minimum)



if __name__=="__main__":
    for _ in range(int(input())):
        # arr_len=int(input())
        arr=list(map(int,input().strip().split()))
        # s=int(input())
        minimum_subset_sum_diffrence(sorted(arr))
        # if check_if_two_suset_have_same_sum(sorted(arr), arr_len):
        #     print("YES")
        # else:
        #     print("NO")

