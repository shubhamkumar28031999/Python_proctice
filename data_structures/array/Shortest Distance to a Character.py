class Solution:
    def shortestToChar(self, s, c):
        index=[]
        l=len(s)
        for i in range(l):
            if s[i]==c:
                index.append(i)
        temp=[10**9]*l
        for i in index:
            temp[i]=0
            t=i-1
            k=1
            while t>-1 and s[t]!=c:
                temp[t]=min(temp[t],k)
                k+=1
                t-=1
            t=i+1
            k=1
            while t<l and s[t]!=c:
                temp[t]=min(temp[t],k)
                k+=1
                t+=1
        return temp

a=Solution()
s = "loveleetcode"
c = "e"
print(a.shortestToChar(s,c))