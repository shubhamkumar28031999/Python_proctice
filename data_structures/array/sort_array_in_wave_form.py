def wave_form(arr):
    length = len(arr)-1
    arr=quickSort(arr,0,length)
    return reverse_alt(arr)


def quickSort(arr,l,h):
    if(l<h):
        j=partition(arr,l,h)
        quickSort(arr,l,j)
        quickSort(arr,j+1,h)
    return arr


def partition(arr,l,h):
    pivot = arr[l];
    i = l
    j = h
    while i<j:
        while arr[i] <= pivot and i<len(arr)-1:
            i+=1
        while arr[j] > pivot and j >= 0:
            j-=1
        if(i<j):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
    temp = arr[l]
    arr[l] = arr[j]
    arr[j] = temp
    return j

def reverse_alt(arr):
    length=len(arr)//2
    for i in range(length):
        temp = arr[2*i+1]
        arr[2*i+1]=arr[2*i]
        arr[2*i]=temp
    return arr

arr =[1,2,12,5,20,4,10,11]
arr = wave_form(arr)
print(arr)