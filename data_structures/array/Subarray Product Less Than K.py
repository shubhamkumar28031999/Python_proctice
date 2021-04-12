import math

from itertools import permutations
class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        l=len(nums)
        ans = 0
        product = 1
        num = 0
        left = 0
        right = 0
        if k < 1:
            return 0
        while right < l:
            product *= nums[right]
            print(f"product up={product}")
            while product >= k:
                if left == l:
                    return ans
                product /= nums[left]
                print(f"product down={product}")
                left += 1
                print(f"left={left}   and   right={right}")

                num -= 1
                print("---------")
            num += 1
            right += 1
            ans += num

            print(f"ans={ans}  num={num}")
            print("=============================================================")
        return ans

if __name__=="__main__":
    nums = [10, 5, 2, 6]
    print(Solution().numSubarrayProductLessThanK(nums,100))