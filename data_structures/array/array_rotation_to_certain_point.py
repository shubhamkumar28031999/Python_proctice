def shiftbyone(arr):
    l= len(arr)
    temp = arr[0]
    for i in range(l-1):
        arr[i]=arr[i+1]
    arr[l-1]=temp


def array_rotate(arr,index):
    for i in range(index):
        shiftbyone(arr)

def display(arr):
    print(arr)

# arr[:2]=[0,5,7]
# print(arr)
# array_rotate(arr,3)
# display(arr)


# -------------------method 2--------------------
def reverse_array(arr,start,end):
   while start<end:
       temp = arr[start]
       arr[start]=arr[end]
       arr[end]=temp
       start+=1
       end-=1

def leftrotate(arr,index):
    reverse_array(arr,0,index-1)
    reverse_array(arr,index,len(arr)-1)
    reverse_array(arr,0,len(arr)-1)

# -------------------circular method-----------
def circular(arr,index):
    i=0

    while i<=index:
        # print(arr)
        temp = arr[0]
        j = 0
        while j < len(arr)-1:
            arr[j]=arr[j+1]
            j+=1
        arr[len(arr)-1]=temp
        i+=1


arr = [1,2,3,4,5,6,7]
index=3
circular(arr,index)
# leftrotate(arr,index)
display(arr)