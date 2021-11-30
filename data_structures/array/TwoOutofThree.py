class Solution:
    def twoOutOfThree(self, nums1, nums2, nums3):
        dic={}
        nums1=list(set(nums1))
        nums2=list(set(nums2))
        nums3=list(set(nums3))
        for i in nums1:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for i in nums2:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for i in nums3:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        ans=[]
        for key,val in dic.items():
            if val>=2:
                ans.append(key)
        return ans
        