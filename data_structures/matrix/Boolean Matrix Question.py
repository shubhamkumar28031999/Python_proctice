def manupulation(matrix):
    r=len(matrix)
    c=len(matrix[0])
    row=[0]*r
    col=[0]*c
    for i in range(r):
        for j in range(c):
            if matrix[i][j]==1:
                row[i]=1
                col[j]=1
    for i in range(r):
        for j in range(c):
            if row[i]==1 or col[j]==1:
                matrix[i][j]=1
    return matrix

def printMatrix(matrix):
    for val in matrix:
        print(val)

if __name__=="__main__":
    martix=[[1,0,0],
            [0,0,0],
            [0,0,1]]
    matrix=manupulation(martix)
    printMatrix(matrix)
