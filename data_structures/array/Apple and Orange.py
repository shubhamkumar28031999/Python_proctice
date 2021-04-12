if __name__=="__main__":
    s,t=map(int,input().strip().split())
    a,b=map(int,input().strip().split())
    m,n=map(int,input().strip().split())
    arr1=list(map(int,input().strip().split()))
    arr2=list(map(int,input().strip().split()))
    count1=0
    count2=0
    for val in arr1:
        if a+val<=t and a+val>=s:
            count1+=1
    for val in arr2:
        if b+val<=t and b+val>=s:
            count2+=1
    print(count1)
    print(count2)



