def missingNumbers(arr, brr):
    arr_dict=dict()
    for val in brr:
        if val in arr_dict:
            arr_dict[val]+=1
        else:
            arr_dict[val]=1
    for val in arr:
        arr_dict[val]-=1
    result=[]
    for key,val in arr_dict.items():
        if key in arr_dict:
            for _ in range(val):
                result.append(key)
        else:
            result.append(key)
    return sorted(result)



if __name__ == "__main__":
    brr=[11,4,11,7,3,7,10,13,4,8,12,11,10,14,12]
    arr=[11,4,11,7,13,4,12,11,10,14]
    print(missingNumbers(arr,brr))