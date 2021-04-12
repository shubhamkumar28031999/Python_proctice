from collections import Counter
class Solution:
    def minNumberOfFrogs(self, croakOfFrog):
        l=len(croakOfFrog)
        d=[]
        dic={'c':'r','r':'o','o':'a','a':'k' }
        i=0
        frog=0
        while i<l:
            if croakOfFrogs[i]=='c':
                d.append(['c'])
            else:
                flag=1
                for val in d:
                    if len(val)<5 and dic[val[-1]]==croakOfFrogs[i]:
                        val.append(croakOfFrogs[i])
                        flag=0
                        break
                if flag==1:
                    return -1
            if croakOfFrogs[i]=='k':
                frog-=1
            i += 1
            frog = max(frog, len(d))
        for val in d:
            if val != ['c','r','o','a','k']:
                return -1
        return frog



s=Solution()
croakOfFrogs ="ccrcroakorakoak"
print(s.minNumberOfFrogs(croakOfFrogs))