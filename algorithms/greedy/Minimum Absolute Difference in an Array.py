import sys

def minimumAbsoluteDifference(arr):
    l=len(arr)
    abs_min=sys.maxsize
    for i in range(l-1):
        for j in range(i+1,l):
            abs_min=min(abs_min,abs(arr[i]-arr[j]))
    return abs_min

if __name__=="__main__":
    arr=[1,-3,71,68,17]
    print(minimumAbsoluteDifference(arr))