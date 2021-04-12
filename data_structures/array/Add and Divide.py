from math import floor
def convert(a,b):
    if a==b:
        return 2
    if a<b:
        return 1
    if a>b:
        if a%b!=0:
            return 1+convert(floor(a/b), b)
        if a%b==0:
            return 1+convert(a, b+1)

for _ in range(int(input())):
    a,b=map(int, input().split())
    print(convert(a,b))


# from math import floor, ceil
# import math
# def convert(a,b):
#     if a==b:
#         return 2
#     if a<b:
#         return 1
#     if a>b:
#         if a%b!=0:
#             return 1+convert(floor(a/b), b)
#         elif a%b==0:
#             return 1+convert(a, b+1)
# def pp(a,b):
#     if a==b:
#         return 2
#     if a<b:
#         return 1
#     if a>b:
#         if b>1:
#             return ceil(math.log(a,b))
#         elif b==1:
#             return ceil(math.log(a, b+1))
#
#
# def solve(a,b):
#     return min(convert(a,b), pp(a,b))
#
#
# for _ in range(int(input())):
#     a,b=map(int, input().split())
#     print(solve(a,b))
