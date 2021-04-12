
def SieveOfEratosthenes(n):
    prime = [True for i in range( n +1)]
    p = 2
    arr=[]
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+ 1, p):
                prime[i] = False
        p += 1
    for p in range(2, n + 1):
        if prime[p]:
            arr.append(p)
    return arr


for _ in range(int(input())):
    n=int(input())
    prim=SieveOfEratosthenes(n)
    l=len(prim)
    for i in range(l-2):
        if prim[i]+prim[i+1]<=n:
            for j in range(i+1,l-1):
                if prim[i]+prim[j]>n:
                    break
                elif prim



