def matrix(R,C,arr):
    lst=[]
    for i in range(R):
        lst.append(arr[C*i:(i+1)*C])
    return lst

def spiral_tarversal(R,C,arr):
    r=0
    c=0
    lst=[]
    while R>r and C>c:
        for i in range(c,C):
            lst.append(arr[r][i])
        r+=1
        for i in range(r,R):
            lst.append(arr[i][C-1])

        C-=1
        if (r<R):
            for i in reversed(range(c,C)):
                lst.append(arr[R-1][i])
            R-=1
        if (c<C):
            for i in reversed(range(r,R)):

                lst.append(arr[i][c])
            c+=1
    return lst


if __name__=="__main__":
    for _ in range(int(input())):
        R,C=map(int,input().split())
        arr=list(map(int,input().split()))
        arr=matrix(R,C,arr)
        print(spiral_tarversal(R,C,arr))