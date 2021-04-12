def min_sum(m,n):
    if m==0:
        if m==1:
            return 0
        else:
            return 'Not Possible'
    elif (n*9)<m:
        return 'Not Possible'
    else:
        res=[0 for i in range(m)]
        n-=1
        for i in range(m-1,0,-1):
            if n>9:
                res[i]=9
                n-=9
            else:
                res[i]=n
                n=0
        res[0] = n + 1

        for val in res:
            print(val,end='')












if __name__=="__main__":
    m=3
    n=23
    min_sum(m,n)