class Solution:
    def countAndSay(self, n):
        if n==1:
            return '1'
        if n==2:
            return '11'
        else:
            sub_string=self.countAndSay(n-1)
            i=1
            l=len(sub_string)
            first=sub_string[0]
            while i<l and first==sub_string[i]:
                i+=1
            return str(i)+first+sub_string[i:]



if __name__=="__main__":
    s=Solution()
    for i in range(1,10):
        print(s.countAndSay(i))