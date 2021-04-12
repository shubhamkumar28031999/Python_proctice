from itertools import permutations,combinations
class Solution:
    def smallestDistancePair(self, nums, k):
        l=len(nums)
        nums.sort()
        lst=[]
        current_pos=0
        perm=combinations([x for x in range(l)],2)
        for x,y in perm:
            lst.append(abs(nums[x]-nums[y]))
            current_pos+=1
            if current_pos==k:
                return lst[current_pos-1]
        # lst.sort()
        # # print(lst)
        # return lst[k-1]

# arr=nums
#         nums.sort()
#         diff=[]
#         n=len(nums)
#         for i in range(n-1):
#             for j in range(i+1,n):
#                 d=abs(arr[j]-arr[i])
#                 diff.append(d)
#         diff.sort()
#         return diff[k-1]

if __name__=="__main__":
    nums=[1,3,1]
    k=1
    print(Solution().smallestDistancePair(nums,k))