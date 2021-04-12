class Solution:
    def removeCoveredIntervals(self, intervals):
        count=0
        lst=[]
        for x,y in intervals:
            if x not in lst and y not in lst:
                lst.extend([x for x in range(x,y)])
            else:
                count+=1
        return count


if __name__=="__main__":
    intervals = [[1,2],[1,4],[3,4]]
    print(Solution().removeCoveredIntervals(intervals))