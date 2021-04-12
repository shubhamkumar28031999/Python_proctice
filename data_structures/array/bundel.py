def knapSack(W, wt, val, n):
    if n == 0 or W == 0:
        return 0
    if (wt[n - 1]>W):
        return knapSack(W, wt, val, n - 1)
    else:
        return max(
            val[n - 1] + knapSack(
                W - wt[n - 1], wt, val, n - 1),
            knapSack(W, wt, val, n - 1))

if __name__=="__main__":
    n=int(input())
    m=int(input())
    bundle1=[]
    bundle2=[]
    for i in range(m):
        bundle1.append(int(input()))
    k = int(input())
    for i in range(k):
        bundle2.append(int(input()))

    print(knapSack(n,bundle1,bundle2,m))