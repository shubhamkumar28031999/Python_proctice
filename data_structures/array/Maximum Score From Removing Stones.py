# class Solution:
#     def solve(self,a,b,c):
#         arr=[a,b,c]
#         arr=sorted(arr)
#         maximum=arr[2]
#         middle=arr[1]
#         minimum=arr[0]
#         return maximum-1,middle-1,minimum
#     def maximumScore(self, a, b, c):
#         ans=0
#         while (a!=0 and b!=0) or (b!=0 and c!=0) or (c!=0 and a!=0):
#             ans+=1
#             a,b,c=self.solve(a,b,c)
#             # print(a,b,c)
#         return ans
# s=Solution()
# a = 2
# b = 4
# c = 6
# print(s.maximumScore(a,b,c))

x="abcd"
for i in x:
    print(i.upper())