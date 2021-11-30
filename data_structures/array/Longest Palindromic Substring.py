class Solution:
    def longestPalindrome(self, s):
        l=len(s)
        max_len=0
        ans=""
        for i in range(l):
            k=0
            while i-k>=0 and i+k<l and s[i-k] == s[i+k] :
                if 2*k+1>max_len:
                    max_len=2*k+1
                    ans=s[i-k:i+k+1]
                k+=1
        for i in range(l):
            k=0
            while i-k>=0 and i+k+1<l and s[i-k]==s[i+k+1]:
                if 2*k + 2 > max_len:
                    max_len=2*k+2
                    ans=s[i-k:i+k+2]
                k+=1
        return ans

if __name__=="__main__":
    s = "babad"
    k=Solution()
    print(k.longestPalindrome(s))