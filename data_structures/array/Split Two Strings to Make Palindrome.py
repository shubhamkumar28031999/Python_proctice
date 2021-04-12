class Solution:
    def checkPalindromeFormation(self, a, b):
        l_a=len(a)
        if l_a==1:
            return True
        else:
            i,j=0,l_a-1
            while i<j and a[i]==b[j]:
                i,j=i+1,j-1
            if a[i:j + 1] == a[i:j + 1][::-1]:
                return True
            if b[i:j + 1] == b[i:j + 1][::-1]:
                return True

            i,j=0,l_a-1
            while i<j and a[j]==b[i]:
                i, j = i + 1, j - 1
            if a[i:j + 1] == a[i:j + 1][::-1]:
                return True
            if b[i:j + 1] == b[i:j + 1][::-1]:
                return True
            return False

if __name__=="__main__":
    print(Solution().checkPalindromeFormation("abdef","fecab"))
