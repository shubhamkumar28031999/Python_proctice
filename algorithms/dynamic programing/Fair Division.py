for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    count1=0
    count2=0
    s=sum(arr)
    for val in arr:
        if val==1:
            count1+=1
        else:
            count2+=1
    if s%2==0:
        if (s//2)%2==0 or ((s//2)%2!=0 and count1!=0):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
