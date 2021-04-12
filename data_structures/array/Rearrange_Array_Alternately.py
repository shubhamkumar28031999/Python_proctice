if __name__=="__main__":
    t = int(input())
    for i in range(t):
        num=int(input())
        arr=list(map(int,input().strip().split()))
        if len(arr)%2==0:
            count=0
            while count<len(arr)//2:
                print(arr[-(count+1)],end=" ")
                print(arr[count],end=" ")
                count+=1
        else:
            count=0
            while count<len(arr)//2:
                print(arr[-(count+1)],end=" ")
                print(arr[count],end=" ")
                count+=1
            print(arr[count])
        print()