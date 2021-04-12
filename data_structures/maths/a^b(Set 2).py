import math
if __name__=="__main__":
    t=int(input())
    for i in range(t):
        a,b = list(map(int,input().strip().split()))
        print(a**b)