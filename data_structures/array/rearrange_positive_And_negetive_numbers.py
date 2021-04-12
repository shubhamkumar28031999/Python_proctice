def pivote(arr):
    i=0
    l=len(arr)-1
    while i<l:
        while arr[i]>0:
            i+=1
        while arr[l]<0:
            l-=1
        if(i<l):
            temp = arr[i]
            arr[i]=arr[l]
            arr[l]=temp
    return rearrange(arr,i)

def rearrange(arr, i):

    if i > (len(arr)/2):

        for j in range(0,len(arr)-i):
            temp = arr[2*j+1]
            arr[2 * j + 1] = arr[i+j]
            arr[i+j] =temp

    else:

        for j in range(0,i):
            temp = arr[2*j+1]
            arr[2 * j + 1] = arr[i+j]
            arr[i+j] =temp

    return arr

arr=[-1,2,-3,4,-5,-6,-7,-8,9]
print(pivote(arr))