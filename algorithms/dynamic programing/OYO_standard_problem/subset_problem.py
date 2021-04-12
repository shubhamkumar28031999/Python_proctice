def is_subset(arr,n):
    left_sum=0
    for val in arr:
        left_sum+=val
    right_sum=0
    for i in range(n-1,-1,-1):
        

if __name__=="__main__":
    arr=[1,5,5,11]
    n=4
    is_subset(arr,n)