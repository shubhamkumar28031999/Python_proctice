def lis(arr,n):
    lis = [1] * n
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] >= arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
    maximum = 0
    for i in range(n):
        maximum = max(maximum, lis[i])
    return n-maximum

for _ in range(int(input())):
    n=int(input())
    s=list(input())

    print(lis(s,n))