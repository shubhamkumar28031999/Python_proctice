def solve(arr,l,r,k):
    if k>0 and k<=r-l+1:
        pos=partition(arr,l,r)

def partition(arr,l,r):
    x = arr[r]
    i = l
    for j in range(l, r):
        if (arr[j] <= x):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    print(arr)
    return i


if __name__=="__main__":
    n=int(input())
    arr=list(map(int,input().split()))
    k = int(input())
    print(solve(arr,0,n-1,k))