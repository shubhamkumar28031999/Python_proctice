
import collections

class Solution:


    def minIncrementForUnique(self, A):
        count= collections.Counter(A)
        supporting_Array=[]
        ans=0
        for x in range(max(A)+len(A)):
            if count[x] >= 2:
                supporting_Array.extend([x] * (count[x] - 1))
            elif supporting_Array and count[x] == 0:
                ans += x - supporting_Array.pop()
        return ans





if __name__=="__main__":
    # arr=[1,2,2]
    arr=[4,4,7,5,1,9,4,7,3,8]
    print(Solution().minIncrementForUnique(arr))