class Solution:
    def reverseString(self, s):
        if len(s)==1:
            return s
        else:
            return [s[-1]] + self.reverseString(s[:-1])

s=Solution()
a=["h","e","l","l","o"]
print(s.reverseString(a))
