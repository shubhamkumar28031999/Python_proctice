from collections import Counter
if __name__=="__main__":
    low=int(input())
    high=int(input())
    arr=[]
    for i in range(low,high+1):
        temp=list(str(i))
        arr.extend(temp)
    arr=Counter(arr)
    ans=0
    for val in arr.values():
        if val==1:
            ans+=1
    print(ans)


