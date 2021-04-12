import sys
def matrix_chain_order_recursive_without_DP(arr,i,j):
    if i==j:
        return 0
    min=sys.maxsize
    for k in range(i,j):
        count=matrix_chain_order_recursive_without_DP(arr,i,k)+\
              matrix_chain_order_recursive_without_DP(arr,k+1,j)+\
              arr[i-1]*arr[k]*arr[j]
        if count<min:
            min=count
    return min

# def matrix_chain_order_DP(arr,n):
#     dp=[[0 for _ in range(n)] for _ in range(n)]
#     for i in range(1,n):
#         dp[i][i]=1
#     for L in range(2,n):



if __name__=="__main__":
    arr=[1, 2, 3, 4]
    n=len(arr)
    # print(matrix_chain_order_recursive_without_DP(arr,1,n-1))
    print(matrix_chain_order_DP(arr,n))