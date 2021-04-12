def product_sub_array(arr):
    length= len(arr)
    i = 0
    array=[]
    while i <length:
        for j in range(length-i):
            # array.append(arr[i:j+i+1])
            temp=1
            for k in arr[i:j+i+1]:
                temp = temp*k
            array.append(temp)
        i+=1
    temp=1
    for i in array:
        temp=temp*i
    return temp

array= [10,3,7]
print(product_sub_array(array))