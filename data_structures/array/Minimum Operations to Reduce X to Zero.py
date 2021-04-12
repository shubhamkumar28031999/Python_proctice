import sys
class Solution:
    def minOperations(self, nums, x):
        if nums[0]<=x or nums[-1]<=x:
            l=len(nums)
            remainder=sum(nums)-x
            if remainder==0:
                return l
            else:
                ans=sys.maxsize
                for i in range(l):
                    temp_len=0
                    curr_sum=0
                    j=i
                    while j<l and curr_sum<remainder:
                        curr_sum+=nums[j]
                        temp_len+=1
                        if curr_sum==remainder:
                            ans=min(ans,l-temp_len)
                        j+=1
                if ans==sys.maxsize:
                    return -1
                else:
                    return ans
        else:
            return -1

s=Solution()
nums = [8828,9581,49,9818,9974,9869,9991,10000,10000,10000,9999,9993,9904,8819,1231,6309]
x = 134365
print(s.minOperations(nums,x))