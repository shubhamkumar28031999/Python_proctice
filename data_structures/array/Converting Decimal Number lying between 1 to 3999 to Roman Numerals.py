class Solution:
    def intToRoman(self, num):
        m = ["", 'M', 'MM', 'MMM']
        c = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM "]
        x = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        i = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        s=m[num//1000]+c[(num%1000)//100]+x[(num%100)//10]+i[num%10]
        return s

s=Solution()
s.intToRoman(100)

