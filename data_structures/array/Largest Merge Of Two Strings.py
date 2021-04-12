class Solution:
    def solve(self,word1,word2,result):
        if word1[0]>=word2[0]:
            if len(word1)>1:
                result+=word1[0]
                return word1[1:],word2,result
            else:
                return "", word2, result+word1
        else:
            if len(word2)>1:
                result+=word2[0]
                return word1,word2[1:],result
            else:
                return word1,"",result+word2
    def solve3(self,word1,word2,result):
        if word1[0]>word2[0]:
            if len(word1)>1:
                result+=word1[0]
                return word1[1:],word2,result
            else:
                return "", word2, result+word1
        else:
            if len(word2)>1:
                result+=word2[0]
                return word1,word2[1:],result
            else:
                return word1,"",result+word2
    def solve2(self,word,result):
        return "",result+word
    def solve4(self,word1,word2,result):
        w1,w2,r1=self.solve(word1,word2,result)
        z1,z2,r2=self.solve3(word1,word2,result)

        if r1>r2:
            return w1,w2,r1
        else:
            return z1,z2,r2
    def largestMerge(self, word1, word2):
        result=""
        while len(word1)>0 or len(word2)>0:
            print(result)
            if word1!="" and word2!="":
                word1,word2,result=self.solve4(word1,word2,result)
            elif word1=="":
                word2,result=self.solve2(word2,result)
            elif word2=="":
                word1,result=self.solve2(word1,result)
        return result

s=Solution()

word1 ="abcabc"
word2 ="abdcaba"
print(s.largestMerge(word1,word2))
