
def findFreeinterval(arr, N):
    if N < 1:
        return
    P = []
    arr.sort(key=lambda a: a[1])
    print(arr)
    for i in range(1, N):
        prevEnd = arr[i - 1][1]
        currStart = arr[i][0]
        if prevEnd <= currStart:
            P.append([arr[i - 1][0],arr[i][0]])
    for i in P:
        print(i)


def solve(l):
    p1=[]
    sum=l[0][3]
    tt=l[0][1]
    ee=l[0][2]
    for i in range(1,len(l)):
        if l[i][1]>tt:
            p=l[i][3]
            sum=sum+p
            tt=l[i][2]
        p1.append(sum)
        if l[i][1]<tt:
            sum1=l[0][3]+l[i][3]
            p1.append(sum1)
    return max(p1)

if __name__ == "__main__":
    # Given List of intervals
    arr = [[1,1, 2,50], [2,3, 5,20],
           [3,6, 19,100], [4,2, 100,200]]

    N = len(arr)
    print(solve(arr))