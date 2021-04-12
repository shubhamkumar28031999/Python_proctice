def prime_Number(num):
    for i in range(2,(num+2)//2):
        if num%i==0:
            return False
    return True

if __name__=="__main__":
    low=int(input())
    high=int(input())
    temp_Arr=[]
    for i in range(low,high):
        if prime_Number(i):
            temp_Arr.append(i)
    print(temp_Arr)
    l=len(temp_Arr)
    count=0
    for i in range(l-1):
        for j in range(i+1,l):
            if temp_Arr[j]-temp_Arr[i]==6:
                count+=1
                break
    print(count)