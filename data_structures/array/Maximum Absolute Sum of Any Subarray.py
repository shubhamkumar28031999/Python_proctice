class Solution:
    def kadane_algorith_max(self,arr):
        max_curr = max_global = arr[0]
        for i in range(1, len(arr) - 1):
            max_curr = max(arr[i], max_curr + arr[i])
            if max_curr > max_global:
                max_global = max_curr
        return max_global
    def kadane_algorith_min(self,arr):
        max_curr = max_global = arr[0]
        for i in range(1, len(arr) - 1):
            max_curr =min(arr[i], max_curr + arr[i])
            max_global=min(max_global,max_curr)
        return max_global

    def maxAbsoluteSum(self, nums):
        return max(abs(self.kadane_algorith_max(nums)),abs(self.kadane_algorith_min(nums)))

s=Solution()
nums = [2,-5,1,-4,3,-2]
print(s.maxAbsoluteSum(nums))

