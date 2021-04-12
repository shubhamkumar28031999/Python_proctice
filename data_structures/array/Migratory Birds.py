def migratoryBirds(arr):
    global max_key
    d= dict()
    for val in arr:
        if val in d:
            d[val]+=1
        else:
            d[val]=1
    max_val=0
    for key,val in d.items():
        if val>max_val:
            max_val=val
            max_key=key
    print(max_key)


if __name__=="__main__":
    arr=[1,2,3,4,5,4,3,2,1,3,4]
    migratoryBirds(arr)