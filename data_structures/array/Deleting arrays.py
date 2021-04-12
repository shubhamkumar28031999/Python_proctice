from math import ceil
for _ in range(int(input())):
    N,K=map(int,input().split())
    print(ceil(N/(K+K+1)))