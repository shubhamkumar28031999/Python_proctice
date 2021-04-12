class Solution:
    def findKthPositive(self, arr, k):
        d={}
        l=len(arr)
        for i in range(1,l+k+1):
            d[i]=0
        for val in arr:
            d[val]=1
        i=0
        for key,val in d.items():
            if val==0:
                i += 1
                if i==k:
                    return key
s=Solution()
arr = [1,2,3,4]; k = 2
print(s.findKthPositive(arr,k))



