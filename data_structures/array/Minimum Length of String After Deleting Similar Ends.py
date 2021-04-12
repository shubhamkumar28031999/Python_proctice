class Solution:
    def minimumLength(self, s):
        l=len(s)
        if l==0:
            return 0
        else:
            if s[0]!=s[-1]:
                return l
            else:
                while len(s)>1 and s[0]==s[-1]:
                    temp=s[0]
                    i=0
                    # print(s)
                    while i<len(s)-1 and s[i]==s[1+i]:
                        i+=1
                    if len(s)-1==i:
                        return 0
                    s = s[i + 1:]
                    if len(s)>0:
                        i=len(s)-1
                        while i>=0 and s[i]==s[i-1]:
                            i-=1
                        s=s[:i]
            # print(s)
            return len(s)

s=Solution()
k="bbbbbbbbbbbbbbbbbbbbbbbbbbbabbbbbbbbbbbbbbbccbcbcbccbbabbb"
print(s.minimumLength(k))
