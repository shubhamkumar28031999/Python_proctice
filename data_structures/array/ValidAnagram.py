from collections import Counter
class Solution:
    def isAnagram(self, s, t):
        if  len(s) != len(t):
            return False
        
        for i in set(s):
            print(s.count(i))
            if s.count(i) != t.count(i):
                return False
        return True






        # s,t=list(s),list(t)
        # s=Counter(s)
        # for i in t:
        #     if i not in s:
        #         return False
        #     else:
        #         s[i]-=1
        #         if s[i]==-1:
        #             return False
        # for i in s.values():
        #     if i!=0:
        #         return False
        # return True




k= Solution()
s = "anagram"
t = "nagaram"
print(k.isAnagram(s,t))