def Solution(n,S,T):
    d1 = {}
    for i in range(n):
        if S[i] == '?':
            pass
        else:
            if S[i] in d1:
                d1[S[i]] += 1
            else:
                d1[S[i]] = 1
    d2={}
    for i in range(n):
        if T[i] == '?':
            pass
        else:
            if T[i] in d:
                d[T[i]]-=1
            else:
                d

for _ in range(int(input())):
    n=int(input())
    S=input()
    T=input()
    print(Solution(n,S,T))