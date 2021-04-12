def solve(n,arr,x):
    while len(arr)!=1:
        temp=x-1
        arr.pop(temp%len(arr))
    return arr[0]

if __name__=="__main__":
    n,x=5,10
    arr=[1,2,3,4,5]
    print(solve(n,arr,x))