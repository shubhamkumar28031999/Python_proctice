def function(arr):
    length=len(arr)
    array=[]
    j=0
    for i in range(length):
        if arr[i]<0:
            array.append(arr[i])
        else:
            pass
    for i in range(length):
        if arr[i]>=0:
            array.append(arr[i])
        else:
            pass

    return array


arr=[-1,6,2,-4,-5,9,-10]
print(function(arr))