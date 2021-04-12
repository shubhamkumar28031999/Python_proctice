class Solution:
    def longestConsecutive(self, nums):
        l=len(nums)
        if l==1:
            return 1
        else:
            nums=set(nums)
            nums=sorted(list(nums))
            print(nums)
            ans=0
            i=0
            while i<len(nums):
                j=nums[i]
                while j+1 in nums:
                    j+=1
                ans=max(ans,j-nums[i]+1)
                if j-nums[i]==0:
                    i+=1
                else:
                    i+=j-nums[i]+1
            return ans

    def longestConsecutive2(self, nums):
        s=set(nums)
        ans=0
        for num in nums:
            if num in s:
                s.remove(num)
                left,right=num,num
                while left-1 in s:
                    left=left-1
                    s.remove(left)
                while right+1 in s:
                    right=right+1
                    s.remove(right)
                ans=max(ans,right-left+1)
        return ans
s=Solution()
nums = [0,3,7,2,5,8,4,6,0,1]
print(s.longestConsecutive2(nums))