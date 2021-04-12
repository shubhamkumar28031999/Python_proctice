import math
def solve (n,k):
        if n == 1:
            return k
        elif n == k:
            return 1
        else:
            if n > k:
                k = math.ceil(n / k) * k
                rem = k % (n)
                if rem == 0:
                    return k // n
                else:
                    return k // n + 1
            if n < k:
                rem = k % n
                if rem == 0:
                    return k // n
                else:
                    return k // n + 1

for _ in range(int(input())):
    n,k=map(int,input().split())
    print(solve(n,k))
