def perfect_sum_array(arr,value):
    array=[]
    for i in range(len(arr)):
        sub_array=[]
        for j in range(i+1):
             sub_array.append(arr[j])
        array.append(sub_array)

arr=[5, 10, 12, 13, 15, 18]
print(perfect_sum_array(arr,30))