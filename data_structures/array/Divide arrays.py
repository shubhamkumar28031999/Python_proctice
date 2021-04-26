MAXN = 100001

def constructMEX(arr, N):
    hash = [0] * MAXN
    for i in range(N):
        hash[arr[i]] = 1
    MexOfArr = 0
    for i in range(1, MAXN):
        if (hash[i] == 0):
            MexOfArr = i
            break
    B = [0] * N
    for i in range(N):
        if (arr[i] < MexOfArr):
            B[i] = arr[i]
        else:
            B[i] = MexOfArr
    return B


def diffrence(arr,N):
    temp_arr=constructMEX(arr,N)
    n=0
    print(temp_arr)
    for i in range(N):
        if arr[i]!=temp_arr[i]:
            n+=1
    return n




for _ in range(int(input())):
    N=int(input())
    arr = list(map(int,input().split()))
    for i in range(N):
        print(diffrence(arr[:i],i),diffrence(arr[i:],N-i))
        if diffrence(arr[:i],i) == diffrence(arr[i:],N-i):
            print(i)
            break
# 0 2 2 3 0