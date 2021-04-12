class Solution:
    def threeSum(self, nums,target):
        l=len(nums)
        count=(10**9)+7
        ans=0
        nums.sort()
        for i in range(l-2):
            j,k=i+1,l-1
            while j<k:
                s=nums[j]+nums[k]+nums[i]
                if s<target:
                    temp = abs(target - s)
                    if count > temp:
                        ans = s
                        count = temp
                    j+=1
                elif s>target:
                    temp= abs(target - s)
                    if count>temp:
                        ans=s
                        count=temp
                    k-=1
                elif s==target:
                    return target
        return ans

s=Solution()
nums = [-1,2,1,-4]
target = 1
print(s.threeSum(nums,target))
