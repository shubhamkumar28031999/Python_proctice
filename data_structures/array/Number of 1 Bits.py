
class Solution:
    def hammingWeight(self, n):
        print(bin(n))
        n=list(str(n))

        return n.count("1")

s=Solution()
n =10
print(s.hammingWeight(n))