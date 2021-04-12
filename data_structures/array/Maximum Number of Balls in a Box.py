class Solution:
    def s(self,n):
        ans=0
        n=str(n)
        for i in range(len(n)):
            ans+=int(n[i])
        return ans
    def countBalls(self, lowLimit, highLimit):
        d={}
        for i in range(lowLimit,highLimit+1):
            s=self.s(i)
            if s in d:
                d[s]+=1
            else:
                d[s]=1
        return max(d.values())

s=Solution()
print(s.countBalls(5,15))