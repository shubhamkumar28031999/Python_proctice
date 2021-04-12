for _ in range(int(input())):
    n= int(input())
    arr= list(map(int,input().split()))
    odd_count=0
    for val in arr:
        if val%2==1:
            odd_count+=1
    if odd_count%2==0:
        print(1)
    else:
        print(2)