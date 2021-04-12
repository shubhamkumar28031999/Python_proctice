def FindIntersection(strArr):
    l=len(strArr)-1
    strArr=strArr[1:l]
    l=l-1
    mid=strArr.index('"',1)
    first_set=set(map(int,strArr[1:mid].split(",")))
    second_set=set(map(int,strArr[mid+4:l-1].split(",")))
    left=sorted(list(first_set.intersection(second_set)))
    strArr=''
    for val in left:
        strArr+=str(val)+','
    return strArr[:-1]

# keep this function call here
print(FindIntersection(input()))