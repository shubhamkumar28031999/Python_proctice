class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1 or n==2:
            return n
        return self.climbStairs(n-1)+self.climbStairs(n-2)

s=Solution()
print(s.climbStairs(7))