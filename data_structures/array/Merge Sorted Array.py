class Solution:
    def merge(self, nums1, m: int, nums2, n: int):
        diff = len(nums1) - n
        for i in range(n):
            nums1[diff] = (nums2[i])
            diff += 1
        nums1.sort()
        return nums1
s=Solution()

nums1=[1,2,3,0,0,0]
m=3
nums2=[2,5,6]
n=3
print(s.merge(nums1,m,nums2,n))
print(nums1)
