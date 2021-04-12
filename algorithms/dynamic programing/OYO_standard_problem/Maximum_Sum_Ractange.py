import sys
def kadane_algorithm(arr):
    l=len(arr)
    current_sum=global_sum=arr[0]
    for i in range(1,l):
        current_sum=max(arr[i],arr[i]+current_sum)
        if current_sum>global_sum:
            global_sum=current_sum
    return global_sum

def maximum_sum_rectange(matrix):
    row=len(matrix)
    col=len(matrix[0])
    max_current=max_global=-sys.maxsize
    for i in range(col):
        temp_arr=[0 for _ in range(row)]
        for j in range(col):
            temp_arr=[(temp_arr[l]+matrix[l][j]) for l in range(row)]
            max_current=max(max_current,kadane_algorithm(temp_arr))
            if max_current>max_global:
                max_global=max_current
    print(max_global)



if __name__=="__main__":
    arr=[
        [1,1,1,0,0],
        [0,-20,1,1,0],
        [1,1,1,1,1],
        [1,1,1,1,1]
    ]
    maximum_sum_rectange(arr)