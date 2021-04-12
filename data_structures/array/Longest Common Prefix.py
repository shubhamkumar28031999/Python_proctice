class Solution:
    def LCP(self,prefix,val):
        l=min(len(prefix),len(val))
        i=0
        while i<l and prefix[i]==val[i]:
            i+=1
        return prefix[:i] if i else ""

    def longestCommonPrefix(self, strs):
        prefix=strs[0]
        for val in strs[1:]:
            if prefix=="":
                return prefix
            prefix=self.LCP(prefix,val)
        return prefix
s=Solution()
strs = ["dog","racecar","car"]
print(s.longestCommonPrefix(strs))