def breakingRecords(scores):
    min_val=scores[0]
    max_val=scores[0]
    min_count=0
    max_count=0
    for val in scores[1:]:
        if max_val<val:
            max_count+=1
            max_val=val
        if min_val>val:
            min_count+=1
            min_val=val
    print(max_count)
    print(min_count)


if __name__=="__main__":
    arr=[3,4,21,36,10,28,35,5,24,42]
    breakingRecords(arr)