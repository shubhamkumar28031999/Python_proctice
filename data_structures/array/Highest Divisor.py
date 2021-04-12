def solve(n):
    for i in range(10,0,-1):
        # print(i)
        if n%i==0:
            return i

n=int(input())
print(solve(n))
