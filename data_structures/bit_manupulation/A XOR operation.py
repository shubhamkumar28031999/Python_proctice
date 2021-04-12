import math
def togglebit(n):
    if (n == 0):
        return 1
    i = n
    n = n | (n >> 1)
    n |= n >> 2
    n |= n >> 4
    n |= n >> 8
    n |= n >> 16

    return i ^ n
def xnor(num1, num2):
    if (num1 < num2):
        temp = num1
        num1 = num2
        num2 = temp
    num1 = togglebit(num1)
    return num1 ^ num2

for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    for i in range(n-1):
        arr[i+1]=xnor(arr[i],arr[i+1])
    print(arr[-1])
