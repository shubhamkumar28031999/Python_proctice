class Solution:

    def myAtoi(self, s: str) -> int:
        if s is None or len(s) < 1:
            return 0
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        s = s.lstrip()
        i = 0
        isNegative = len(s) > 1 and s[0] == '-'
        isPositive = len(s) > 1 and s[0] == '+'
        if isNegative or isPositive:
            i += 1
        number = 0
    
        while i < len(s) and '0' <= s[i] <= '9':
            number = number * 10 + (ord(s[i]) - ord('0'))
            i += 1
        # Give back the sign to the number
        if isNegative:
            number = -number
        # Edge cases - integer overflow and underflow
        if number < INT_MIN:
            return INT_MIN
        if number > INT_MAX:
            return INT_MAX
        return number

            
               


s = "+-56"
print(Solution().myAtoi(s))
