class Solution:
    def areNumbersAscending(self, s) -> bool:
        s=s.split()
        temp=-32652
        for val in s:
            if val.isdigit():
                if int(val)<=temp:
                    return False
                temp=int(val)
        return True



s = "4 5 11 26"
k=Solution()
print(k.areNumbersAscending(s))