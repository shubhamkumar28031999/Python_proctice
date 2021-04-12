import math
if __name__=="__main__":
    n=int(input())
    arr=[]
    for i in range(n):
        ls=list(map(str,input().strip().split()))
        arr.append(ls)
    count_of_D=0
    for i in range(n):
        for j in range(n):
            if arr[i][j]=="D":
                count_of_D+=1
            else:
                pass
    max_cube=int(math.sqrt(count_of_D))
    print(max_cube)