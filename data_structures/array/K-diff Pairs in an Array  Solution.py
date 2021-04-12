from itertools import combinations

class Solution:
    def findPairs_slow(self, nums, k):
        lst=set()
        indices=combinations([x for x in range(len(nums))],2)

        for x,y in indices:
            if abs(nums[x]-nums[y])==k:
                if nums[x]>nums[y]:
                    lst.add((nums[x],nums[y]))
                else:
                    lst.add((nums[y],nums[x]))
        # print(lst)
        return len(lst)

    def findPairs(self,nums,k):
        nums.sort()
        l=len(nums)
        lst=set()
        for i in range(l-1):
            j=i+1
            while j<l and abs(nums[i]-nums[j])<=k:
                if abs(nums[i]-nums[j]) ==k:
                    if nums[i] > nums[j]:
                        lst.add((nums[i], nums[j]))
                    else:
                        lst.add((nums[j], nums[i]))
                j+=1
        # print(lst)
        return len(lst)


if __name__=="__main__":
    nums = [1,3,1,5,4]
    k = 0
    print(Solution().findPairs(nums,k))