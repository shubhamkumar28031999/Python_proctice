from collections import Counter
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if A==B:
            c=Counter(A)
            for val in c.values():
                if val>=2:
                    return True
            return False
        else:

            l_A=len(A)
            l_B=len(B)
            if l_A!=l_B:
                return False
            else:
                d = []
                for i in range(l_A):
                    if A[i]!=B[i]:
                        d.append([A[i],B[i]])
                if len(d)==2:

                    if d[0][0]==d[1][1] and d[0][1]==d[1][0]:
                        print(d)
                        return True
                return False


s=Solution()
A = "ab"
B = "ca"
print(s.buddyStrings(A,B))