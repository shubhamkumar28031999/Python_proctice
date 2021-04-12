class Solution:
    def missingNumber(self, nums):
        l=len(nums)
        s= (l*(l+1)) // 2
        nums=sum(nums)
        return abs(s-nums)

if __name__=="__main__":
    nums = [3, 0, 1]
    print(Solution().missingNumber(nums))