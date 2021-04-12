def partition(arr,l,h):
    if h > l:
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

def quickSort(arr,low,high):

        print(f"form quick sort low={low} and high={high}")
        pi =partition(arr,low,high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n= int(input())
        arr = list(map(int, input().strip().split()))
        quickSort(arr,0,len(arr)-1)
        for i in range(len(arr)):
            print(arr[i],end=" ")
        print()
