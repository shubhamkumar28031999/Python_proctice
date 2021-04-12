import sys
class Solution:
    def Diff(self,li1, li2):
        return (list(list(set(li1) - set(li2)) + list(set(li2) - set(li1))))
    def minCharacters(self, a, b):
        a=list(a)
        b=list(b)
        l_a=len(a)
        l_b=len(b)
        operations=sys.maxsize
        max_a=max(a)
        max_b=max(b)
        count=0
        for i in range(l_b):
            if b[i]<=max_b:
                count+=1
        operations=min(operations,count)
        count=0
        for i in range(l_a):
            if  a[i]<max_a:
                count+=1
        operations=min(operations,count)
        print(self.Diff(a,b))
        operations=min(len(self.Diff(a,b)),operations)
        return operations

a="dabadd"
b="cda"
s=Solution()
print(s.minCharacters(a,b))

