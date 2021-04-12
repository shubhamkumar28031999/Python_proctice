def pickingNumbers(a):
    b=set(a)
    arr=[]
    for temp in b:
        count_1_neg=0
        count_1_pos=0
        for val in a:
            if temp-1 == val or temp==val:
                count_1_neg+=1
            if temp+1 == val or temp==val:
                count_1_pos+=1
        arr.append(max(count_1_neg,count_1_pos))
    return max(arr)



if __name__=="__main__":
    a=[1,2,2,3,1,2]
    print(pickingNumbers(a))