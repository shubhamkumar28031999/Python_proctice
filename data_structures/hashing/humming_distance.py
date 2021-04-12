def hammingDistance(n1, n2):
    x = n1 ^ n2
    setBits = 0

    while (x > 0):
        setBits += x & 1
        x >>= 1

    return setBits

if __name__=="__main__":
    N,M=list(map(int,input().strip().split()))
    arr_A=list(map(int,input().strip().split()))
    arr_B=list(map(int,input().strip().split()))
    for i in range(M):
        u,v=list(map(int,input().strip().split()))
        temp=arr_A[u-1]
        arr_A[u - 1]=arr_A[v-1]
        arr_A[v-1]=temp
    d={}
    for i in range(N):
        t=(arr_A[i],arr_B[i])
        d[t]=hammingDistance(arr_A[i],arr_B[i])
    print(min(min(d)))


