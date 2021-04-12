import math
import collections
for _ in range(int(input())):
    n=int(input())
    arr=sorted(list(map(int,input().split())))
    count=0
    for i in range(1,len(arr)):
        for j in range(i):
            if arr[i]>arr[j]:
                # print(f"arr[i]={arr[i]} and arr[j]={arr[j]}")
                count+=1
                break

    print(count)

