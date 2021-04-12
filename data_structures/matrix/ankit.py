if __name__=="__main__":
    row,col,puch=map(int,input().split())
    dict={}
    for _ in range(row):
        temp=list(map(int,input().split()))
        for val in temp:
            if val in dict:
                dict[val]+=1
            else:
                dict[val]=1
    arr=[]
    for x,y in dict.items():
        if y>=3:
            arr.append(x)
    print(sorted(arr))


