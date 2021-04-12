from collections import Counter
class Solution:
    def findLHS(self, nums):
        res=0
        count=Counter(nums)
        for val in count:
            if val+1 in count:
                res=max(res,count[val]+count[val+1])
        return res
s=Solution()
nums = [1,2,3,4]
print(s.findLHS(nums))
