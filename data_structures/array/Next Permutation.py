from itertools import permutations
import math
class Solution:
    def nextPermutation(self, nums):
        temp=nums
        temp=sorted(temp)
        all_perm=list(permutations(temp))
        all_perm=[list(perm) for perm in all_perm]
        l = len(all_perm)
        i=l-all_perm[::-1].index(nums)-1


        if i==l-1:
            next_val= all_perm[0]
        else:
            next_val= all_perm[i+1]
        l=len(next_val)
        for i in range(l):
            nums[i]=next_val[i]
        return next_val

s=Solution()
arr=[1,5,1]
print(s.nextPermutation(arr))

