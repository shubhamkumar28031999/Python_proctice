def segregate(arr):
    length=len(arr)-1
    start=0
    end=length
    while start<end:
        if arr[start]%2==1:
            temp=arr[start]
            arr[start]=arr[end]
            arr[end]=temp
            end-=1
        else:
            start+=1
    print(arr)

arr=[1,4,5,3,8,6,10,2]
segregate(arr)