class Solution:
    def isPalindrome(self, x: int) -> bool:

        if str(x)==str(x)[::-1]:
            return True
        else:
            return False

n=-121
s=Solution()
print(s.isPalindrome(n))