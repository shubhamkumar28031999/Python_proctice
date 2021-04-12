class Solution:
    def plusOne(self, digits):
        l=len(digits)
        digits[-1]=digits[-1]+1
        carry=0
        for i in range(l-1,-1,-1):
            sum=(carry+digits[i])
            carry=sum//10
            digits[i]=sum%10
        if carry==0:
            return digits
        else:
            return [1]+digits



s=Solution()
arr=[4,3,2,1]
print(s.plusOne(arr))