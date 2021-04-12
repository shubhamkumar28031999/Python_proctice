def birthday(s, d, m):
    count=0
    if m!=1:
        for i in range(len(arr)-m+1):
            temp_sum=0
            temp_Arr=s[i:i+m]
            print(temp_Arr)
            for j in temp_Arr:
                # print(temp_sum)
                temp_sum+=j
            if temp_sum==d:
                count+=1
    else:
        count=s.count(d)
    return count

if __name__=="__main__":
    arr=[5,2,2,1,5,3,2]
    print(birthday(arr,9,3))