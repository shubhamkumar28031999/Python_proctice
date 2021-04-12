import sys
class Solution:
    def restoreArray(self, adjacentPairs):
        arr=[]
        arr.extend(adjacentPairs[0])
        arr.sort()
        adjacentPairs.remove(adjacentPairs[0])
        l=len(adjacentPairs)+1
        for _ in range(l):
            for val in adjacentPairs:
                if arr[-1]==val[0]:
                    arr.append(val[1])
                    adjacentPairs.remove(val)
                elif arr[-1]==val[1]:
                    arr.append(val[0])
                    adjacentPairs.remove(val)
                elif arr[0]==val[0]:
                    arr.insert(0,val[1])
                    adjacentPairs.remove(val)
                elif arr[0]==val[1]:
                    arr.insert(0,val[0])
                    adjacentPairs.remove(val)
        return arr


        return arr

s=Solution()
adjacentPairs = [[4,-10],[-1,3],[4,-3],[-3,3]]
print(s.restoreArray(adjacentPairs))