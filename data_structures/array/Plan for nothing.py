if __name__=="__main__":
    num=int(input())
    arr=[0 for x in range(10**6)]
    for _ in range(num):
        temp = list(map(int,input().split()))
        for val in temp:
            arr[val]+=1
    l=1
    for i in range(1,10**6):
        if arr[i]==0:
            print(i)
            l=0
            break

    if l==1:
        print(-1)



# 4
# 2 1 2 3 5
# 2 1 3 5 7
# 2 1 3 4 5
# 2 3 6 11 12
