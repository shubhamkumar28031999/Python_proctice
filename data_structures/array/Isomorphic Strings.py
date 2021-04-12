
from collections import deque
class Solution:
    def isIsomorphic(self, X: str, Y: str) -> bool:
        queue=deque()
        queue.appendleft()
        X=list(X)
        Y=Y.split(" ")
        # print(Y)
        if len(X) != len(Y):
            return False
        dict = {}
        s = set()
        for i in range(len(X)):
            x = X[i]
            y = Y[i]
            if x in dict:
                if dict[x] != y:
                    return False
            else:
                if y in s:
                    return False
                dict[x] = y
                s.add(y)
        return True

s="abba"
t = "dog cat cat dog"
obj=Solution()
print(obj.isIsomorphic(s,t))
