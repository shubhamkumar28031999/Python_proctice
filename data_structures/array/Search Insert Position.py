class Solution:
    def searchInsert(self, nums, target):
        try:
            k=nums.index(target)
        except:
            i=0
            for j in range(len(nums)):
                if nums[j]>target:
                    break
                i+=1
            return i

    def strStr(self, haystack, needle):
        return haystack.find(needle)

nums = [1,3,5,6]
target = 2
haystack = "hello"
needle = "llh"
s=Solution()
print(s.strStr(haystack,needle))