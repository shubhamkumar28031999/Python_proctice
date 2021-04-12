if __name__=="__main__":
    n=int(input())
    arr=list(map(int,input().strip().split()))
    for _ in range(int(input())):
        a,b=map(int,input().strip().split())
        count=0
        bitwise=arr[a]
        for i in range(a+1,b):
            bitwise=bitwise&arr[i]
        if bitwise !=0:
            print(count)
        else:
            





