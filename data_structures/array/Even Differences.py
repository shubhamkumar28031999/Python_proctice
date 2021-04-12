for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    even=0
    odd=0
    for val in arr:
        if val%2==0:
            even+=1
        else:
            odd+=1
    if even>odd:
        print(odd)
    else:
        print(even)