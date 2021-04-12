class Solution:
    def combinationSum(self, candidates, target):
        candidates.sort()
        l=len(candidates)
        result = [[x] for x in candidates]
        




if __name__=="__main__":
    arr=[1,2,3,4]
    target=8
    print(Solution().combinationSum(arr,target))