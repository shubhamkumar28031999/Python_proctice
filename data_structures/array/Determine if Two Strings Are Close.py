from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str):
        if word1==word2:
            return True
        else:

            l_1=len(word1)
            l_2=len(word2)
            if l_1!=l_2:
                return False
            else:
                d1 = {}
                for i in range(l_1):
                    if word1[i] not in d1:
                        d1[word1[i]]=1
                    else:
                        d1[word1[i]]+=1
                
                for i in range(l_1):
                    if word2[i] not in d:
                        d[word2[i]]=1
                    else:
                        d[word2[i]]+=1
                for val in d.values():
                    if val%2==1:
                        return False
                return True
