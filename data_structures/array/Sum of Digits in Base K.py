# class Solution:
#     def sumBase(self, num: int, base: int):
#         base_num = ""
#         while num > 0:
#             dig = int(num % base)
#             if dig < 10:
#                 base_num += str(dig)
#             else:
#                 base_num += chr(ord('A') + dig - 10)
#             num //= base
#         base_num = base_num[::-1]
#         base_num=str(base_num)
#         ans=0
#         for i in range(len(base_num)):
#             ans+=int(base_num[i])
#         return ans
#
#
#
# n,k=map(int,input().split())
# s=Solution()
# print(s.sumBase(n,k))
n,k=map(int,input().split())
arr= list(map(int,input().split()))
if k in arr:
    print(1)
else:
    print(-1)