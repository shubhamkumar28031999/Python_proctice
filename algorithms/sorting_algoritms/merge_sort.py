def mergeSort(arr):
    if len(arr)>1:
        mid= len(arr)//2

        l_arr=arr[:mid]
        r_arr=arr[mid:]
        mergeSort(l_arr)
        mergeSort(r_arr)

        i=j=k=0
        while(i<len(l_arr) and j<len(r_arr)):
            if(l_arr[i]<r_arr[j]):
                arr[k]=l_arr[i]
                i+=1

            else:
                arr[k]=r_arr[j]
                j+=1
            k += 1
        while i<len(l_arr):
            arr[k]=l_arr[i]
            k+=1
            i+=1
        while j<len(r_arr):
            arr[k]=r_arr[j]
            k+=1
            j+=1


arr=[4,2,7,1,9,3]
mergeSort(arr)
print(arr)

