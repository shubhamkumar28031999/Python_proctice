class Solution:
    def sumOfUnique(self, nums):
        d={}
        for val in nums:
            if val in d:
                d[val]+=1
            else:
                d[val]=1

        sum=0
        for key,val in d.items():
            if val==1:
                sum+=key
        return sum

s=Solution()
nums = [1, 2, 3, 4, 5]
print(s.sumOfUnique(nums))
