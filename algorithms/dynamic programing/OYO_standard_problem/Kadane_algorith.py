def kadane_algorith(arr):
    max_curr=max_global=arr[0]
    for i in range(1,len(arr)-1):
        max_curr=max(arr[i],max_curr+arr[i])
        if max_curr>max_global:
            max_global=max_curr
    print(max_global)
def smallestSubWithSum(arr, n, x):
    # Initialize current sum and minimum length
    curr_sum = 0
    min_len = n + 1

    # Initialize starting and ending indexes
    start = 0
    end = 0
    while (end < n):

        # Keep adding array elements while current
        # sum is smaller than x
        while (curr_sum <= x and end < n):
            curr_sum += arr[end]
            end += 1

        # If current sum becomes greater than x.
        while (curr_sum > x and start < n):
            if (end - start < min_len):
                min_len = end - start
            curr_sum -= arr[start]
            start += 1

    return min_len

if __name__=="__main__":
    arr=[12,3,14,56,77,12]
    sum=100
    print(smallestSubWithSum(arr,len(arr),100))