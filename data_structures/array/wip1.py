
def solve(mat,n):
    time=0
    s1=""
    s2=""
    for i in range(n):
        if mat[i][0]>=time:
            s1+="c"+str(i)+"-"
            time+=mat[i][1]
        else:
            s2+="c"+str(i)+"-"
    return s1[:len(s1)-1],s2[:len(s2)-1]



mat=[
    [0,1],
    [2,1],
    [2,4],
    [5,3],
    [6,2],
    [7,5],
    [9,4]
]
l=7
print(solve(mat,l))

