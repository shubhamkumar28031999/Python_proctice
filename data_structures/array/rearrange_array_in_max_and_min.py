def rearrange(arr):
    length=len(arr)-1
    start=0
    end=length
    while end>start:
        if start%2==0:
            temp=arr[end]
            arr[end]=arr[start]
            arr[start]=temp
            start+=1
            end-=1
        else :
            temp=arr[length]
            arr[length]=arr[start]
            arr[start]=temp
            start+=1
    print(arr)

arr=[1,2,3,4,5,6,7,8,9]
rearrange(arr)