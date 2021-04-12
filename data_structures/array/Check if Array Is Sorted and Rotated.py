class Solution:
    def check(self, nums):
        l=len(nums)
        i=0
        while i<l-1 and nums[i]<=nums[i+1]:
            i+=1
        nums=nums+nums[:i+1]
        nums=nums[i+1:]
        i=0
        while i<l-1 and nums[i]<=nums[i+1]:
            i+=1
        if i==l-1:
            return True
        else:
            return False
s=Solution()
nums = [2,1]
print(s.check(nums))
