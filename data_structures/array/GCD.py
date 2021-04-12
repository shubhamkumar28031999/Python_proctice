class Solution:
    def gcd(self, A, B):
        if A%B==0:
            return B
        return self.gcd(B,A%B)

s=Solution()
print(s.gcd(20,6))