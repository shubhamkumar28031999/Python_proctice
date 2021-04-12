def divisibleSumPairs(n, k, ar):
    count=0
    for i in range(n-1):
        for j in range(i+1,n):
            print(f"arr[{i}]={ar[i]}   and   arr[{j}]={ar[j]}    sum={ar[i]+ar[j]}")
            if (ar[i]+ar[j])%k==0:
                count+=1
    return count

if __name__=="__main__":
    arr=[1,3,2,6,1,2]
    print(divisibleSumPairs(6,3,arr))