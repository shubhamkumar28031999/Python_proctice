import math
def isPerfectSquare(x):
    # if x >= 0,
    if (x >= 0):
        sr = math.sqrt(x)

        # return boolean T/F
        return ((sr * sr) == x)
    return False

s=0
for _ in range(int(input())):
    x,y=map(int,input().split())
    s+=x**y
arr=[]
for i in range(1,s//2 +1):
    if s%i==0:
        arr.append(i)
arr.append(s)
perfect_squre=0
for val in arr:
    temp=isPerfectSquare(val)
    if temp:
        perfect_squre+=math.sqrt(val)
print(perfect_squre)
