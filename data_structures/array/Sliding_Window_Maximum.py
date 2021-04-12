def function(arr,value):
    length = len(arr)
    array=[]
    for i in range(length-value+1):
        array.append(max(arr[i:i+value]))
    return array


arr = [1, 2, 3, 1, 4, 5, 2, 3, 6]
print(function(arr,3))
