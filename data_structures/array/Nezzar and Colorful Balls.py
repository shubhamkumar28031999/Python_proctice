from collections import Counter
for _ in range(int(input())):
    n=int(input())
    arr= list(map(int,input().split()))
    count=Counter(arr)
    print(max(count.values()))