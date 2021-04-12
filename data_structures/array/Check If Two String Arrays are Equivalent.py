class Solution:
    def arrayStringsAreEqual(self, word1, word2):
        world1="".join(word1)
        l=len(world1)
        world2=''
        i=0
        while i<l:
            temp=''
            flag=False
            for val in word2:
                if val[0]==world1[i]:
                    if val==world1[i:i+len(val)]:
                        world2+=val
                        flag=True
                        i+=len(val)
            if flag==False:
                return False
        return True

s=Solution()
word1=["abc", "d", "defg"]; word2 = ["abcddefg"]
print(s.arrayStringsAreEqual(word1,word2))

