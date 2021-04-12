class Solution:
    def threeSum(self, nums):
        l=len(nums)
        count=set()
        nums.sort()
        for i in range(l-2):
            target=-nums[i]
            j,k=i+1,l-1
            while j<k:
                s=nums[j]+nums[k]
                if s<target:
                    j+=1
                elif s>target:
                    k-=1
                else:
                    count.add((nums[i],nums[j],nums[k]))
                    j+=1
                    k-=1
        count=list(count)
        for i in range(len(count)):
            count[i]=list(count[i])
        return sorted(count)

s=Solution()
nums = [-1, 0, 1, 2, -1, -4]

print(s.threeSum(nums))
