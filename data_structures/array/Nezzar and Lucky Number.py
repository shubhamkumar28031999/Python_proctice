def CheckForSequence(arr, k) :
    for i in range(len(arr) - 1, -1, -1) :
        if (k >= arr[i]) :
            k -= arr[i]
    if (k != 0) :
        return False
    else :
        return True

for _ in range(int(input())):
    n,d=map(int,input().split())
    arr=list(map(int,input().split()))
    m=max(arr)
    temp = []
    for i in range((m // d) + 1):
        if (10 * i) + d > m:
            break
        temp.append(((10 * i) + d) % 10)

    for val in arr:
        if val%10 ==d:
            print("YES")
        else:
            if CheckForSequence(temp,val):
                print('YES')
            else:
                print("NO")
