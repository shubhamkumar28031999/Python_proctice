import math
for _ in range(int(input())):
    n=int(input())
    temp=math.log2(n) - int(math.log2(n))
    if n>1 and temp!=0:
        print('YES')
    else:
        print("NO")