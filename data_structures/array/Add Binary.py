class Solution:
    def addBinary(self, a, b):
        return  bin(int(a,2)+int(b,2)).replace('0b','')


s=Solution()
a='11'
b='1'
print(s.addBinary(a,b))