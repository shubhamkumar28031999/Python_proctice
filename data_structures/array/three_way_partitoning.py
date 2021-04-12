def partitioning(arr,low,high):
    length=len(arr)-1
    start=0
    end=length
    for i in range(length):
        if arr[i]<low:
            temp=arr[start]
            arr[start]=arr[i]
            arr[i]=temp
            start+=1

        if arr[i]>high:
            temp = arr[end]
            arr[end] = arr[i]
            arr[i] = temp
            end-=1

        else:
            pass
    print(arr)

arr=[4,2,9,3,6,0,10,12,1,18]
partitioning(arr,6,10)
