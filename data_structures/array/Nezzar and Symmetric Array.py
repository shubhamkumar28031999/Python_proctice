from collections import Counter
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    c=Counter(arr)
    flag=True
    for val in c.values():
        if val%2!=0:
            flag=False
            break
    if flag:
        print("YES")
    else:
        print("NO")